당신은 s/w 아키텍트입니다. 
요구 사항은 아래와 같습니다.  DIP, OCP,  SRP 에 의한 클래스를 설계하려고 합니다.
템플릿 엔진을 사용하여 템플릿 파일을 관리하는 클래스를 설계합니다.
1. 엔진은 jinja2을 사용합니다.   
2. 템플릿 파일은 report_template.html와 email_template.html 이 있고, 추후에 추가될 될 수 있습니다.  
3. report_template.html 인 경우,  
   - 변수들은 general_information, summary, detail 그룹으로 되어 있고,
   - group별 변수들을 추출할 수 있는 api 을 제공해줍니다.
   - json 형식으로 저장되어 있는 context 에서 summary와 detail의 url들을 추출하는 api를 제공합니다
   - json 파일의 내용 중 특정 변수를 변경하는 api를 제공합니다
4. email_template.html 인 경우,
   - 일반적 렌터링 함수만 제공 합니다
5. context 는 json 형식으로 파일시스템에 저장하고 삭제 등 관리합니다.
   - 파일위치 및 이름은 template/<템플릿이름>/context_<버전>.json 으로 저장합니다.



7. template html 관리
7.1 report_template.html
``` html
<!DOCTYPE html>
<html>
<head>
    <title>{{ general_information.title }}</title>
</head>
<body>
  <h1>{{ general_information.heading }}</h1>
    Hello<br>
    We share the status of {{ general_information.version }} test results in {{ general_information.week }}th week of {{ general_information.year }} year.<br>
    <br>
  <h2>Test Environment Information</h2>
    <ul>
      <li>System Version: {{ general_information.version }}</li>
    <br>
  <h2>Message from Test Team</h2>
    <p>{{ general_information.message }}</p>
    <br>
  <h2>Summary of Product</h2>
  <ul>
    {% for summary in product_summaries %}
      <li>{{ summary.name }}: {{ summary.url }} {{ summary.top }} {{ summary.left }} {{ summary.width }} {{ summary.height }}</li>
    {% endfor %}
  </ul>
  <h2>Detailed Test Results</h2>
    <ul>
      {% for detail in details %}
        {% if detail.enable %}
          <li>{{ detail.name }}: {{ detail.url }} {{ detail.top }} {{ detail.left }} {{ detail.width }} {{ detail.height }}</li>
        {% endif %}
      {% endfor %}
    </ul>
</body>
</html>

```
7.2 email_template.html
``` html
<!DOCTYPE html>
<html>
<head>
    <title>Email Template</title>
</head>
<body>
    <h1>Hello, {{ recipient }}</h1>
    <p>This is a test email.</p>
</body>
</html>
```


