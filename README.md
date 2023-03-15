<br>
<p style="margin-left: 40px;">Приветствую!</p>

<p style="margin-left: 40px;">Это тестовое задание для <a href="https://optimacros.com/" target="_blank">Optimacros</a><br>
	&nbsp;</p>
<p style="margin-left: 40px;">Для сбрoки и запуска проекта используйте Docker:<br>
	docker build -t optimacros .<br>
	docker run -d -p 80:80 --name opti optimacros</p>

<p style="margin-left: 40px;">Чтобы посчитать факториал подключитесь к websocket по адресу<br>
	http://localhost:80/ws/factorial/<br>
	И передайте json вида {&quot;request_factorial&quot;: &quot;100000&quot;}<br>
	В ответ придёт json {&quot;request_factorial&quot;: &quot;100000&quot;, &quot;result&quot;: &quot;2.8242294079603476E+456573&quot;}</p>
