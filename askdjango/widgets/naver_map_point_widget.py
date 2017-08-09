import re
from django import forms
from django.template.loader import render_to_string
#from askdjango import settings 절대 이렇게 가져오지말라함. 이거만하면 일부만가져옴.
from django.conf import settings #django/conf/global_settings.py + askdjango/settings.py 이조합된값 가져오는것.

class NaverMapPointWidget(forms.TextInput):
    BASE_LNG, BASE_LAT ='127.0275996','37.4978648' #강남역
    def render(self, name, value, attrs):

        width = str(self.attrs.get('width',800)) # 있으면 width 가져오고 없으면 800 이 말임.
        height = str(self.attrs.get('height',600)) # 가져오고 str로 문자열로바꿔주고.
        if width.isdigit(): width += 'px' # 숫자로만 이루어져있는가? 검사하고 그렇다면 px 붙여줌.
        if height.isdigit(): height += 'px'


        context = {
            'naver_client_id': settings.NAVER_CLIENT_ID,
            'id' : attrs['id'],
            'width': width,
            'height': height,
            'base_lat': self.BASE_LAT,
            'base_lng': self.BASE_LNG,
        }
        
        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+', value)
                context.update({'base_lat': lat, 'base_lng': lng})
            except (IndexError, ValueError):
                pass
        
        
        html = render_to_string('widgets/naver_map_point_widget.html', context)

        attrs['readonly'] = 'readonly' #이거해주면 자바스크립트에의해서만변경가능 즉, 직접 칸을채울수없고 클릭해야함. 
        parent_html = super().render(name, value, attrs)
        
        return parent_html + html