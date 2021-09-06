#   Django Allauth

```

    1.  Instalr Django Allauth
    1.1 Aplicacion de Cliente de OAuth -> Tipo de Aplicacion y sus Caracteristicas 
    2.  http://localhost:8000 -> Orígenes autorizados Google Developer
    3.  http://localhost:8000/accounts/google/login/callback/ -> URL de Redireccionamiento
    3.  Configuraciones en el settings.py 
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
    4.  Social Application -> Cliend ID , Secret Key -> Site solo es informativo
    5.  La pagina de Registrro 'Sign up' tiene algun error que no he econtrado su solucion pero lo arregle
        creando una pagina de registro externa que funciona y la remplace en su redirecciones.
    6.  Para la instalacion de facebook login requiere certificado SSL DJANGO-EXTENSION Werkzeug pyOpenSSL 
        -> AGREGAR AL SETTING django-extension
        http://localhost:8000/accounts/facebook/login/callback/ -> Facebook Valid Redirect
        python manage.py runserver_plus localhost:8000 -- cerf-file/tem/cert - Servidor SSL
        ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https' -> en el Settings

```