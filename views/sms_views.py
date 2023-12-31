from flask import Blueprint
from ..features.ncloudsms import sendmsg
from ..features.gps import get_gps
import json

bp = Blueprint('sms', __name__, url_prefix='/sms')


@bp.route('/')
def sms_route():
    return "sms default page"

@bp.route('/send')
def sms_send(name="홍길동"):

    # gps 위도 경도 불러오기
    lat, lng = get_gps()

    # 공백 제외 최대 80바이트
    response_text = sendmsg(content=name +
                            f"님의 사고가 감지되었습니다. 위치: [{lat}, {lng}] 기존에 저장된 연락처로 전송함.")

    response_json = json.loads(response_text)

    # 메세지 전송 성공여부
    if "202" in response_json["statusCode"]:
        return "success"
    else:
        return "fail"
