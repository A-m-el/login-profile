{% extends "base.html" %}


{% block content %}
<h1>Register</h1>
<form action="{{ url_for('register') }}" method="post">
    {{ form.csrf_token }}
    <p>
        {{ form.name.label }}<br>
        {{ form.name(size=32) }}<br>
        {% for error in form.name.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
    </p>
    <p>
        {{ form.username.label }}<br>
        {{ form.username(size=32) }}<br>
        {% for error in form.username.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
    </p>
    <p>
        {{ form.email.label }}<br>
        {{ form.email(size=64) }}<br>
        {% for error in form.email.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
    </p>
    <p>
        {{ form.password.label }}<br>
        {{ form.password(size=32) }}<br>
        {% for error in form.password.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
    </p>
    <p>
        {{ form.password2.label }}<br>
        {{ form.password2(size=32) }}<br>
        {% for error in form.password2.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
    </p>
    <p>{{ form.register() }}</p>
</form>
{% endblock %}
