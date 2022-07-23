import json
import time
from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute
from loguru import logger

from app.core.logging.Logging import Logging


@logger.catch
class LoggingDependency(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            start_time = time.monotonic()
            try:
                request_parameters = await request.json()
            except:
                request_parameters = request.path_params

            try:
                log_headers = dict(request.headers.items())
            except:
                log_headers = "NA"

            log = {
                "method_url": f"{request.method} {request.url}",
                "Params": request_parameters,
                "headers": log_headers,
                "Client IP": request.client
            }
            try:
                response: Response = await original_route_handler(request)
                api_response = ""
                if response.body.decode() != "":
                    api_response = json.loads(response.body)

                status_code = "NA"
                if hasattr(response, 'status_code'):
                    status_code = response.status_code

                log["Response"] = api_response
                log["status_code"] = status_code
                log["time"] = time.monotonic() - start_time
                log_filename = request.url.path.split("/")[2].strip()
                logging_obj = Logging(f"{log_filename}_request_log")
                logging_obj.logger_class_object.log(log)
            except Exception as exc:
                status_code = 422;
                if hasattr(exc, 'status_code'):
                    status_code = exc.status_code
                log["Response"] = exc
                log["status_code"] = status_code
                log["time"] = time.monotonic() - start_time
                logging_obj = Logging("error")
                logging_obj.logger_class_object.log(log, "ERROR")
                raise exc
            return response

        return custom_route_handler
