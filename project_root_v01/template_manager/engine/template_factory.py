import os

from template_engine import TemplateEngine
from template_manager.context.template_context import TemplateContextManager
from template_manager.engine.report_template_processor import ReportTemplateProcessor
from template_manager.engine.email_template_processor import EmailTemplateProcessor


class TemplateFactory:
    def __init__(self, engine: TemplateEngine):
        self.engine = engine

    def get_processor(self, template_name, version):
        context_manager = TemplateContextManager(self.engine.get_template_dir(), template_name, version)
        if template_name == "report_template":
            return ReportTemplateProcessor(self.engine, context_manager)
        elif template_name == "email_template":
            return EmailTemplateProcessor(self.engine, context_manager)
        else:
            raise ValueError(f"Unknown template: {template_name}")


if __name__ == "__main__":
    # 템플릿 엔진 초기화
    template_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')
    print(template_dir)
    engine = TemplateEngine(template_dir)

    # TemplateFactory에서 report_template.html을 처리하는 Processor 생성
    factory = TemplateFactory(engine)
    processor = factory.get_processor("report_template", "v1")

    # 그룹별 변수 추출
    group_variables = processor.extract_group_variables('general_information')
    print(group_variables)

    # URL 추출
    summary_urls, detail_urls = processor.extract_urls_from_context()
    print(summary_urls)
    print(detail_urls)

    # 템플릿 렌더링
    context = processor.load_context()
    print(context)
    rendered_output = processor.render_template(context)

    print(rendered_output)