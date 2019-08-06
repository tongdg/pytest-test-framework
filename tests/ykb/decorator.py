import os
import allure
from common.utils import Utils
from config import tdg_config
utils = Utils()
import functools

# 截图
def exception_screenshot():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            try:
                return func(*args, **kw)
            except Exception as e:
                driver = kw.get('multi_browser_driver')
                save_file = utils.generate_time + '_excepiton.png'
                save = os.path.join(tdg_config.BASE_PATH, "tests", "ykb", "screenshot",save_file)
                driver.save_screenshot(save)
                file = open(save, 'rb').read()
                allure.attach(body=file, name='错误截图！', attachment_type=allure.attachment_type.PNG)
                raise e
        return wrapper
    return decorator








