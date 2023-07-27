# Future features

## Bugs

### Local configuration

Actualmente hay que correr `ruby dev.rb` y `ruby prod.rb` para alternar en el archivo de configuración entre el tema local (`theme: morel-theme`) y el tema remoto (`remote_theme: morelrep/morel-theme`).

Dado que en la documentación de la gema `remote_theme` no menciona este problema, asumo que el tema remoto debería poderse usar también en la configuración local. Sin embargo, a mí me arroja el siguiente error:

```
/home/morel/.rvm/rubies/ruby-3.0.6/lib/ruby/3.0.0/net/http.rb:612:in `require': cannot load such file -- openssl (LoadError)
Did you mean?  open3

```

El approach que intenté fue usar la opción que ofrece Jekyll para tener configuraciones alternas según el ambiente. Esto se emplea  con la siguiente sintaxis: `bundle exec jekyll serve --config [FILE1,FILE2]`. Sin embargo, esta función no aplica para los themes, pues Jekyll sigue tratando de cargar el tema remoto. 

He probado anular el tema remoto en el `FILE2`(`_config_local.yml`) de varias maneras: `remote_theme:`, `remote_theme: null` y `remote_theme: ""`. Ninguna funciona. En todos los casos, sigue tratando de cargar el tema remoto, y por ende produciendo un error. 

Lo único que funciona es borrar `remote_theme`de `FILE1`(`_config.yml`) cada vez que se corre localmente. Y volverlo a escribir cuando se vuelve a producción. Esto es lo que hacen los scripts `dev.rb`y `prod.rb` respectivamente.

Sería ideal conseguir una solución que no requiera de la ejecución de estos scripts, ni del cambio manual de la línea `remote_theme` en `_config.yml`.

## Enhancements

### CSS changes
  - Rendear el site.title automáticamente
  - Mejorar el rendering del elemento `code`
  - Style the `em` element


### Layout folder changes
  - Link condicional a tener más de un elemento: Actualmente todos los elementos de la metadata (autor(es), editorial, ciudad, repositorio) generan un link, que contiene la lista de obras con el mismo elemento en ellas. El link actualmente se activa siempre. Habría que hacer un cambio para que se active únicamente si hay más de un elemento en ellas.
  - revisar cómo es lo de los distintos favicons por plataforma, como se generan en favicon.io
  - No-image option
  - Torrent download option

# Docs
- * [Migrate](https://import.jekyllrb.com/docs/home/) from your previous system

# Project
- Tener presente estos asuntos legales alrededor del logo, etc: https://www.zettlr.com/press#usage-rights
- Fijar versión máxima y mínima de MOREL en gemfile

<!--

Unclassified:

- Banderitas de nacionalidad
- Página de libros por traductor
- Integración con:
	- Wikipedia
	- HathiTrust
- Agregar en el script de generación: borrar los archivos de página no utilizados

-->
