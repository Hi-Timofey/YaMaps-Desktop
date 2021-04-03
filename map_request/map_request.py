# -*- coding: utf-8 -*-
from PIL import Image
import requests
from io import BytesIO


class MapRequest:
    allowed_params = ['l', 'll', 'z', 'size']
    allowed_attr = ['response_link', 'image_bytes', 'image_pillow']
    api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
    api_url = 'https://static-maps.yandex.ru/1.x/?'

    def get_image(self, pillow=False, bytes_=False):
        self.response_link = f'{MapRequest.api_url}{"&".join([ str(p)+"="+str(self.params[p]) for p in self.params])}'

        response = requests.get(self.response_link)
        if not response:
            raise ValueError(f'Код {response.status_code} ({response.reason})')

        return_ = []
        if pillow:
            image_bytes = response.content
            stream = BytesIO(image_bytes)
            self.image_pillow = Image.open(stream).convert("RGBA")
            stream.close()
            return_.append(self.image_pillow)
        if bytes_:
            self.image_bytes = BytesIO(response.content)
            return_.append(self.image_bytes)

        if len(return_) == 0:
            raise ValueError('Передай в параметры тип возвращяемого объекта!')
        if len(return_) == 1:
            return return_[0]
        return return_

    def __init__(self, **params):
        self.params = {}
        self.response_link = None
        self.image_bytes = None
        for p in params:
            self.__setattr__(p, params[p])

    def __setattr__(self, attr, value):
        if len(self.__dict__) == 0:
            self.__dict__['params'] = {}

        elif attr in MapRequest.allowed_params:
            self.__dict__['params'][f'{attr}'] = value
        # If not allowed - remember anyway
        elif attr in MapRequest.allowed_attr:
            self.__dict__[f'{attr}'] = value
        else:
            raise AttributeError(attr + ' not allowed')

    def __str__(self):
        return f'Map request:'


if __name__ == '__main__':
    # Как использовать:
    req = MapRequest(l='map')
    print(req)
    req.ll = '37.620070,55.753630'
    req.size = '450,450'
    req.l = 'sat'
    req.z = 13
    print(req.params)
    r = req.get_image(bytes_=True)
    print(r, type(r))
