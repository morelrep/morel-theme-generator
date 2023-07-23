## Instructions to install the theme

## Basic {#install}

- Fork the repository. That is, create a copy in your [Github](github.com) account.
- Open your system's terminal in the folder on your local computer where you will be working on the site (Mac and Linux have native terminals. For Windows, you will have to use [WLS](https://learn.microsoft.com/en-us/windows/wsl/install).
- Run `$ git clone http://febr3s.github.io/morel-site-generator` to clone the repository.
- Run `$ cd morel-site-generator` to move to the repository folder
- Run `$ bundle update` to update the theme and its dependencies. If you don't have Ruby on your system, follow the instructions in [Jekyll](https://jekyllrb.com/docs/ruby-101/)
- Run `ruby dev.rb`(alternatively, delete `febr3s.github.io/morel-theme-generator` from the `remote_theme:` line in `_config.yml`)
- Run `$ bundle exec jekyll serve --config _config.yml,_config_local.yml --livereload` to run the test site.

## Customize {#configure}

Now you have on your local computer a ready-made site *with sample content, from the MOREL  site Afro Latin American Writers in Translation ([ALAWiT](https://alawit.org))*. You can run it locally to test with `$ bundle exec jekyll serve --config _config.yml,_config_local.yml --livereload`. 

To fill it with your site's information, follow these steps:

- Open _config.yml in your text editor and change:
  - The `title` to your site's.
  - The `tagline` to your site's.
  - The `email` and/or social media accounts to your site's.
  - The `description` to your site's.
  - The `jotform` link (create your free account at https://www.jotform.com/).
- Replace the logo, raster and avatar files by adding a file to:
  - `assets/img/img/theme/logo.png`
  - `assets/img/img/theme/avatar.jpg`
  - `assets/img/img/theme/plot.png`
- Open the `podcast.md` file and change the title and tagline of your podcast or blog.
- The `_posts` folder has the MOREL posts. Delete the MOREL posts and create your own with [Jekyll nomenclature](https://jekyllrb.com/docs/posts/). If you don't want to add any podcast posts or episodes to your site, change in `_config.yml` the `podcast` value to `false`.

## Generating the content from Zotero {#generate}

- Run `$ jekyll build --config _config_local.yml` to import to the `_sites` folder the updated content generators.
- Run `$ unzip -d ./assets/ ./_site/assets/env.zip` to update the Python environment that generates the contents.
- Open Zotero and review the [guide](#zotero-fields) to make the fields 100 % readable for MOREL.
- Export your Zotero collection as `csv`. If you don't know how to do it follow the instructions [here](https://www.zotero.org/support/kb/exporting). 
- Name your `csv` file as `books_zotero.csv`. Replace the file of the same name found in the `assets/data` folder.
- Run `$ cd assets/env/bin` to go to the folder where the Python environment is activated. Activate it with `$ source activate`.
- Run `$ cd ../src` to move to the folder where the Python scripts are located.
- Run `$ python morel-generate` to generate the content from your Zotero collection.
- Run `$ bundle exec jekyll serve --config _config.yml,_config_local.yml --livereload` to activate the local server for browsing.
- Open the browser and go to the link provided by the local server (usually it's http://127.0.0.1:4000).
- Browse your custom site!

## Deploy {#publish}
- Run `$ ruby prod.rb`(alternatively, add `febr3s.github.io/morel-theme-generator` to the `remote_theme` line:)
- To publish to Github, follow their [instructions](https://docs.github.com/en/pages/quickstart) (ignore the "New repository" step as you are working with your MOREL fork).
- To publish with a third party, follow Jekyll's [instructions](https://jekyllrb.com/docs/deployment/third-party/).
- To publish to your personal server follow Jekyll's [instructions](https://jekyllrb.com/docs/deployment/manual/).

## To install the theme as a local Ruby gem, or without code

We are working on instructions and utilities to facilitate these possibilities. 

### Subscribe to one of our channels to stay updated {#suscribe}:

- [Twitter](https://twitter.com/morelrep)
- Email newsletter
<!-- <script id="mcjs">!function(c,h,i,m,p){m=c.createElement(h),p=c.getElementsByTagName(h)[0],m.async=1,m.src=i,p.parentNode.insertBefore(m,p)}(document, "script", "https://chimpstatic.com/mcjs-connected/js/users/8aec37d971cdc280e8f9eb567/1a19782d38e75f439e3d5a1fd.js");</script>-->
- [Facebook](https://www.facebook.com/morelrep)

## Zotero fields {#zotero-fields}

MOREL items are added in the same way that items are added in any [Zotero library](https://www.zotero.org/support/adding_items_to_zotero). In its current version, MOREL can only process items of type `book`. Since not all the fields needed for MOREL are available for the `book` content type, some considerations must be made:

- Excerpt: the fragment from each MOREL record corresponds to the `notes` of Zotero (see the [documentation] of the notes (https://www.zotero.org/support/notes) of Zotero). In its current version, MOREL *only accepts one excerpt per book*.
- Cover: the cover is a jpg file that is added as an `attachment` to the Zotero item (see the Zotero attachments [documentation](https://www.zotero.org/support/attaching_files)).
- Translation or original: in order to filter translated books from originals, MOREL uses Zotero's `Series` field to indicate whether it is a translation with the `tr` sign.
- First edition: MOREL uses the `Date` field for the date of publication of the book and the `Edition` field for the date of first edition.