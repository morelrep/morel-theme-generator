## Instrucciones para instalar el tema como rep

- forkea el repositorio. Es decir, crea una copia en tu cuenta github
- abre el terminal en el folder de tu computadora local donde trabajarás el sitio
- $ git clone [rep] # clona el repositorio
- $ cd morel-site-generator # te mueves a la carpeta del repositorio
- abre _config.yml en tu editor de texto y:
  - borra la línea `theme: minima`
  - descomenta (borra `#`) de la línea `theme: morel-theme`
- $ bundle install # instala el tema y sus dependencias

Ahora tienes un sitio listo *con el contenido de sample, del sitio MOREL Afro Latin American Writers in Translation (ALAWiT)*. Puedes correrlo localmente para probar con `$ bundle exec jekyll serve`. Para llenarlo con tu propio contenido de Zotero y los datos de tu sitio, sigue los siguientes pasos:

- $ jekyll build # importa a la carpeta _sites los generadores de contenido actualizados
- $ COMANDO # descomprime el archivo "env.zip", que se encuentra en la carpeta assets que acabamos de copiar a main folder
- abre _config.yml en tu editor de texto y:
  - asígnale el `título` a tu sitio
  - asígnale el `tagline` a tu sitio
  - asígnale`email` y/o social media a tu sitio
  - asígnale la `description` a t sitio
  - asígnale el `jotform` link a tu sitio (crea tu cuenta gratuita en https://www.jotform.com/)
- Abre Zotero y exporta tu colección de Zotero como csv. Guárdalo en la carpeta assets/data. Nombra el archivo "books_zotero.csv". Revisa la [guía](#zotero-fields) para llenar las fichas de Zotero 100 % legibles para MOREL.
- $ cd assets/env/bin # ve a la carpeta para activar el ambiente Python
- $ source activate
- $ cd ../src # muévete a la carpeta donde están los scripts de Python
- $ python morel-generate # genera el contenido a partir de tu colección de Zotero
- $ bundle exec jekyll serve --livereload # activa el servidor local para navegar tu sitio!