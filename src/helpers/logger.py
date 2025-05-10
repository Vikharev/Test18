import allure
import json
import logging

from allure_commons.types import AttachmentType

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log(response, request_body=None, allure_logging=False):
    logger.info(f"REQUEST METHOD: {response.request.method}")
    logger.info(f"REQUEST URL: {response.url}")
    logger.info(f"REQUEST HEADERS: {response.request.headers}")
    logger.info(f"REQUEST BODY: {request_body}\n")
    logger.info(f"STATUS CODE: {response.status_code}")
    logger.info(f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000:.0f} ms\n")
    logger.info(f"RESPONSE HEADERS: {response.headers}")
    logger.info(f"RESPONSE BODY: {response.text}\n.\n.")
    if allure_logging:
        allure.attach(
            body=f"URL: {response.request.url}\nMethod: {response.request.method}\nCode: {response.status_code}\n"
                 f"Body: {response.request.body}",
            name="Request",
            attachment_type=AttachmentType.TEXT,
            extension="txt",
        )

        response_json = response.json()
        allure.attach(
            body=json.dumps(response_json, indent=4, ensure_ascii=False),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )

        cookies = {cookie.name: cookie.value for cookie in response.cookies}
        allure.attach(
            body=json.dumps(cookies, indent=4, ensure_ascii=False),
            name='Cookies',
            attachment_type=AttachmentType.TEXT,
            extension='json'
        )