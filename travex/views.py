import json
import requests

from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from loguru import logger


class ActivateUserEmail(APIView):
    def get(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = json.dumps({'uid': uid, 'token': token})
        result = requests.post(post_url, data=post_data, headers={'Content-Type': 'application/json'})
        message = result.text
        if message == '':
            message = "Pereydite w prelozheniye Attaplace"

        return Response(message)


class ResetPasswordView(View):
    def get (self, request, uid, token):
        return render(request, 'reset_password.html')

    def post (self, request, uid, token):
        # logger.warning(request.POST)
        new_password=request.POST.get("new_password")
        re_new_password=request.POST.get("re_new_password")
        payload = json.dumps({
            'uid': uid,
            'token': token,
            'new_password': new_password,
            're_new_password': re_new_password})
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host() + '/'
        password_reset_url = "users/reset_password_confirm/"  # url used for activate user
        password_post_url = web_url + 'auth/' + password_reset_url
        logger.warning(password_post_url)
        logger.warning(payload)
        response = requests.post(password_post_url, data=payload, headers={'Content-Type': 'application/json', })
        return HttpResponse(response.text)


def eula(request):
    html = '''
    </body></html>
        <h2>End-User License Agreement (EULA) of Attaplace</h2>

<p>This End-User License Agreement ("EULA") is a legal agreement between you and Attaplace</p>

<p>This EULA agreement governs your acquisition and use of our Attaplace software ("Software") directly from Attaplace or indirectly through a Attaplace authorized reseller or distributor (a "Reseller").</p>

<p>Please read this EULA agreement carefully before completing the installation process and using the Attaplace software. It provides a license to use the Attaplace software and contains warranty information and liability disclaimers.</p>

<p>If you register for a free trial of the Attaplace software, this EULA agreement will also govern that trial. By clicking "accept" or installing and/or using the Attaplace software, you are confirming your acceptance of the Software and agreeing to become bound by the terms of this EULA agreement.</p>

<p>If you are entering into this EULA agreement on behalf of a company or other legal entity, you represent that you have the authority to bind such entity and its affiliates to these terms and conditions. If you do not have such authority or if you do not agree with the terms and conditions of this EULA agreement, do not install or use the Software, and you must not accept this EULA agreement.</p>

<p>This EULA agreement shall apply only to the Software supplied by Attaplace herewith regardless of whether other software is referred to or described herein. The terms also apply to any Attaplace updates, supplements, Internet-based services, and support services for the Software, unless other terms accompany those items on delivery. If so, those terms apply.</p>

<h3>License Grant</h3>

<p>Attaplace hereby grants you a personal, non-transferable, non-exclusive licence to use the Attaplace software on your devices in accordance with the terms of this EULA agreement.</p>

<p>You are permitted to load the Attaplace software (for example a PC, laptop, mobile or tablet) under your control. You are responsible for ensuring your device meets the minimum requirements of the Attaplace software.</p>

<p>You are not permitted to:</p>

<ul>
<li>Edit, alter, modify, adapt, translate or otherwise change the whole or any part of the Software nor permit the whole or any part of the Software to be combined with or become incorporated in any other software, nor decompile, disassemble or reverse engineer the Software or attempt to do any such things</li>
<li>Reproduce, copy, distribute, resell or otherwise use the Software for any commercial purpose</li>
<li>Allow any third party to use the Software on behalf of or for the benefit of any third party</li>
<li>Use the Software in any way which breaches any applicable local, national or international law</li>
<li>Use the Software for any purpose that Attaplace considers is a breach of this EULA agreement</li>
<li>Post illegal products or services, tobacco and related products, drugs and drug related products, spyware or malware, and prohibited financial products and services.</li>
<li>Post abusive, illegal, sexual, or racist content. Users will be responsible for the actions taken within the application.</li>
<li>To post pictures of your children as we are not taking responsibilities to where the content will be published.</li>

</ul>

<h3>Intellectual Property and Ownership</h3>

<p>Attaplace shall at all times retain ownership of the Software as originally downloaded by you and all subsequent downloads of the Software by you. The Software (and the copyright, and other intellectual property rights of whatever nature in the Software, including any modifications made thereto) are and shall remain the property of Attaplace.</p>

<p>Attaplace reserves the right to grant licences to use the Software to third parties.</p>

<h3>Termination</h3>

<p>This EULA agreement is effective from the date you first use the Software and shall continue until terminated. You may terminate it at any time upon written notice to Attaplace.</p>

<p>It will also terminate immediately if you fail to comply with any term of this EULA agreement. Upon such termination, the licenses granted by this EULA agreement will immediately terminate and you agree to stop all access and use of the Software. The provisions that by their nature continue and survive will survive any termination of this EULA agreement. This EULA was created by <a href="https://www.app-privacy-policy.com/app-eula-generator/">App EULA Template Generator from App-Privacy-Policy.com</a> for Attaplace</p>

<h3>Governing Law</h3>

<p>This EULA agreement, and any dispute arising out of or in connection with this EULA agreement, shall be governed by and construed in accordance with the laws of <span class="country">us</span>.</p>
    <html><body>
    '''
    return HttpResponse(html)