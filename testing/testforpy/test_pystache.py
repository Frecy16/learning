import os
import sys
from mitmproxy import http

# from test_mitmproxy2.template import Template

addon_dir = os.path.dirname(__file__)
sys.path.append(addon_dir)
print(addon_dir)

import os

import pystache


class Template:
    @classmethod
    def render(cls, path, dict):
        render = pystache.Renderer(escape=lambda u: u)
        print(os.path.abspath(os.getcwd()))
        with open(path) as f:
            content = f.read()
            parsed = pystache.parse(content)
            result = render.render(parsed, dict)
            return result


def response(flow: http.HTTPFlow):
    method = flow.request.method
    url = flow.request.pretty_url.split('?')[0]
    params = [{k: v} for k, v in flow.request.query.fields]
    cookies = [{k: v} for k, v in flow.request.cookies.fields]
    data = {
        "method": method.__repr__(),
        "url": url.__repr__(),
        "params": params,
        "cookies": cookies
    }
    print(Template.render(addon_dir + "/test_http.mustache", data))
