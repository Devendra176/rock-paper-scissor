from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from game.models import ThemeAvailable

class GetFrontPage(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        context = self.get_renderer_context()
        return Response(context, template_name='form/form.html')

    def get_renderer_context(self):
        context = super().get_renderer_context()
        context['theme_data'] = ThemeAvailable.objects.all()
        return context
