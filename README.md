# Instructions to install the theme

## Prerequisites

- **Zotero**: Install Zotero reference management software from the [official website](https://www.zotero.org/) and create collections to organize your content.

- **Python**: Install Python programming language from the [official Python website](https://www.python.org/) based on your operating system. Ensure you have Python version 3.x installed.

- **Jekyll**: Install Jekyll, a static site generator, using your preferred method:
  - For macOS or Linux, open a terminal and run the following command:
    ```bash
    $ gem install bundler jekyll
    ```
  - For Windows, follow the installation guide provided on the [Jekyll website](https://jekyllrb.com/docs/installation/windows/).

## Basic {#install}

1. Fork the repository. That is, create a copy in your [Github](github.com) account (alternatively, [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repository. If you choose this option, skip steps 2 and 3).
2. Open your system's terminal in the folder on your local computer where you will be working on the site. Mac and Linux have native terminals. For Windows, you will have to use [WLS](https://learn.microsoft.com/en-us/windows/wsl/install).
3. Run `$ git clone http://github.com/[your_username]/morel-site-generator` to clone the forked repository to your desktop.
4. Run `$ cd morel-site-generator` to move to the repository folder
5. Run `$ bundle install` to install the theme and its dependencies. If you don't have Ruby on your system, follow the instructions in [Jekyll](https://jekyllrb.com/docs/ruby-101/)
6. Run `ruby dev.rb`(alternatively, delete `febr3s.github.io/morel-theme-generator` from the `remote_theme:` line in `_config.yml`)
7. Run `ruby serve-local.rb` (alternatively, `$ bundle exec jekyll serve --config _config.yml,_config_local.yml --livereload`) to run the test site.

## Customize {#configure}

Now you have on your local computer a ready-made site *with sample content, from the MOREL  site Afro Latin American Writers in Translation ([ALAWiT](https://alawit.org))*. You can run it locally to test with `$ bundle exec jekyll serve --config _config.yml,_config_local.yml --livereload`. 

To fill it with your site's information, follow these steps:

- Open _config.yml in your text editor and change:
  - The `title` to your site's.
  - The `tagline` to your site's.
  - The `email` and/or social media accounts to your site's.
  - The `jotform` link (create your free account at https://www.jotform.com/).
- Open the file `_abouts/site-description.md` and write a description for your site. The `<!-- more -->` line splits what is shown on the footer of all your pages from what is shown both in the footer and only on the `about` page. For this to work you have to complete the final step of this section
- Replace the logo, pattern and avatar files by adding a file to:
  - `assets/img/tema/logo.png`
  - `assets/img/tema/avatar.jpg`
  - `assets/img/tema/trama.png`
- Open the `podcast.md` file and change the title and tagline of your podcast or blog.
- The `_posts` folder has the MOREL posts. Delete the MOREL posts and create your own with [Jekyll nomenclature](https://jekyllrb.com/docs/posts/). If you don't want to add any podcast posts or episodes to your site, change in `_config.yml` the `podcast` value to `false`
- Run the site locally with `ruby serve-local.rb` (alternatively, `$ bundle exec jekyll serve --config _config.yml,_config_local.yml --livereload`)
- Open the `_site` folder and copy the file `site-description.html`to the `_includes`folder
- Open the `about.md` file and delete the line `{% raw %}{% include_relative README.md %}{% endraw %}`

## Generating the content from Zotero {#generate}

### Extracting data and scripts

- Run `$ jekyll build --config _config_local.yml` to import to the `_sites` folder the updated content generators.
- Run `$ unzip -d ./assets/ ./_site/assets/env.zip` to update the Python environment that generates the contents.
- Open [Zotero](https://www.zotero.org/) and review the [guide](#zotero-fields) at the end of this instructions to make the fields 100 % readable for MOREL.
- Export your Zotero collection as `csv`. If you don't know how to do it follow the instructions [here](https://www.zotero.org/support/kb/exporting). 
- Name your `csv` file as `books_zotero.csv`. Replace the file of the same name found in the `assets/data` folder.

### Using Python to generate content

- Make sure that you have the [requirements](https://stackoverflow.com/questions/48314010/is-there-a-way-to-automatically-install-required-packages-in-python) on your system
- Install [pip](https://pypi.org/project/pip/) if you don't have it
- Run `$ cd assets/env/bin` to go to the folder where the Python environment is activated. Activate it with `$ source activate`.
- Run `$ cd ../src` to move to the folder where the Python scripts are located.
- Run `$ python3 morel-generate.py` to generate the content from your Zotero collection. In some operating systems, the command might vary. Check the Python documentation for guidance
- Run `cd ../../..`to go to the root folder of the site
- Run `rm ./assets/env`to remove the python environment until the next update. Alternatively, delete the folder using the explorer.
- Run `$ bundle exec jekyll serve --config _config.yml,_config_local.yml --livereload` to activate the local server for browsing.
- Open the browser and go to the link provided by the local server (usually it's http://127.0.0.1:4000).
- Browse your custom site!

## Deploy {#publish}
- Run `$ ruby prod.rb`(alternatively, add `febr3s.github.io/morel-theme` to the `remote_theme` line:)
- To publish to Github, follow their [instructions](https://docs.github.com/en/pages/quickstart) (ignore the "New repository" step as you are working with your MOREL fork).
- To publish with a third party, follow Jekyll's [instructions](https://jekyllrb.com/docs/deployment/third-party/).
- To publish to your personal server follow Jekyll's [instructions](https://jekyllrb.com/docs/deployment/manual/).

<!--- ## To install the theme as a local Ruby gem, or without code

We are working on instructions and utilities to facilitate these possibilities. 

### Subscribe to one of our channels to stay updated {#suscribe}:

- [Twitter](https://twitter.com/morelrep)
- Email newsletter-->
<!-- <script id="mcjs">!function(c,h,i,m,p){m=c.createElement(h),p=c.getElementsByTagName(h)[0],m.async=1,m.src=i,p.parentNode.insertBefore(m,p)}(document, "script", "https://chimpstatic.com/mcjs-connected/js/users/8aec37d971cdc280e8f9eb567/1a19782d38e75f439e3d5a1fd.js");</script>-->
<!--
- [Facebook](https://www.facebook.com/morelrep)-->

## Zotero fields {#zotero-fields}

MOREL items are added in the same way that items are added in any [Zotero library](https://www.zotero.org/support/adding_items_to_zotero). In its current version, MOREL can only process items of type `book`. Since not all the fields needed for MOREL are available for the `book` content type, some considerations must be made:

### Nonexistent fields

- Excerpt: the fragment from each MOREL record corresponds to the `notes` of Zotero (see the [documentation] of the notes (https://www.zotero.org/support/notes) of Zotero). In its current version, MOREL *only accepts one excerpt per book*.
- Cover: the cover is a jpg file that is added as an `attachment` to the Zotero item (see the Zotero attachments [documentation](https://www.zotero.org/support/attaching_files)).

### Tweaked fields

- Series: in order to filter translated books from originals, MOREL uses Zotero's `Series` field to indicate whether it is a translation with the `tr` sign.
- Series Number: in order to filter featured content from regular content, MOREL uses Zotero's `Series Number` field to indicate whether it is featured content with the `fc` sign.
- Date / Edition: MOREL uses the `Date` field for the date of publication of the book and the `Edition` field for the date of first edition.
- Extra: MOREL uses the `Date` field for the place of birth and/or nationality of the author.

### Tweaked fields for downloads

- URL: if there is a dowload available, add the direct link here. You can also upload a backup to archive.org and add the direct link to the archive.org download here
- Archive: Name of the repository where you found the download originally. For example, Cervantes Virtual
- Loc. in Archive: url to the repository where you found the download originally. For example, https://www.cervantesvirtual.com/
- Library Catalog: direct link to the page on worldcat.org with the library information of the title. For example, https://www.worldcat.org/title/poesias-completas-de-placido-gabriel-de-la-concepcion-valdes/oclc/10013286/editions?referer=di&editionsView=true
