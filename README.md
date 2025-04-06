# Instructions to install the theme

## Install {#install}

### Remote (using your web browser)

### Local (using command line) 

- **Fork the repository** — that is, create a copy in your [GitHub](https://github.com) account.
- Open your system's terminal in the folder on your local computer where you will be working on the site. Mac and Linux have native terminals. For Windows, use [WSL (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install).
- Run:  
```
$ git clone https://github.com/[your_username]/morel-theme-generator
```  
to clone the repository.
- Run:  
```
$ cd morel-theme-generator
```  
to move to the repository folder.
- Run:  
```
$ bundle update
```  
to update the theme and its dependencies. If you don't have Ruby on your system, follow the instructions in [Jekyll](https://jekyllrb.com/docs/ruby-101/)
- Run:  
```
$ ruby serve-local.rb
```  
to launch the test site locally.

## Customize {#configure}

You now have a ready-made site *with sample content from the MOREL site Afro Latin American Writers in Translation ([ALAWiT](https://alawit.org))*.

To fill it with your site's information, follow these steps:

- Open `_config.yml` and change:
  - The `title` to your site's.
  - The `tagline` to your site's.
  - The `email` and/or social media accounts to your site's.
  - The `jotform` link (create your free account at https://www.jotform.com/).
- Open the file `_about/site-description.md` and write a description for your site. The `<!-- more -->` line separates what appears in the footer across all pages from the longer description that appears on the `about` page only. For this to work you have to complete the final step of this section.
- Replace the logo, pattern and avatar files by adding a file to:
  - `assets/img/tema/logo.png`
  - `assets/img/tema/avatar.jpg`
  - `assets/img/tema/trama.png`
- Open the `podcast.md` file and change the title and tagline of your podcast or blog.
- The `_posts` folder has the MOREL posts. Delete the MOREL posts and create your own with [Jekyll nomenclature](https://jekyllrb.com/docs/posts/). If you don't want to add any podcast posts or episodes to your site, change in `_config.yml` the `podcast` value to `false`
- Commit the changes and wait for the customized site to deploy. If you are using GitHub in the web browser, just wait the site to deploy. If you are working locally, push the changes to see them online, or test them locally with  
```
$ ruby serve-local.rb
```

## Generating the content from Zotero 

### Remote (using your web browser)

### Local (using command line) 

- Open [Zotero](https://www.zotero.org/) and review the [guide](#zotero-fields) at the end of this instructions to make the fields 100 % readable for MOREL.
- Export your Zotero collection as a `.csv` file. If you don't know how to do it follow the instructions [here](https://www.zotero.org/support/kb/exporting). 
- Name your `.csv` file `books_zotero.csv` and place it inside the `assets/data` folder.
<!--
- Run `$ cd assets/env/bin` to go to the folder where the Python environment is activated. Activate it with `$ source activate`.
- Run `$ cd ../src` to move to the folder where the Python scripts are located.
- Run `$ python3 morel-generate.py` to generate the content from your Zotero collection. In some operating systems, the command might vary. Check the Python documentation for guidance-->
- Run:  
```
$ ruby serve-local.rb
```  
to activate the local server for browsing.
- Open the browser and go to the link provided by the local server (usually it's http://127.0.0.1:4000).
- Browse your custom site!

## Zotero Fields {#zotero-fields}

MOREL items are added in the same way that items are added in any [Zotero library](https://www.zotero.org/support/adding_items_to_zotero). In its current version, MOREL can only process items of type `book`. Since not all the fields needed for MOREL are available for the `book` content type, some considerations must be made:

- Excerpt: the fragment from each MOREL record corresponds to the `notes` of Zotero (see the [documentation](https://www.zotero.org/support/notes) about Zotero notes). In its current version, MOREL *only accepts one excerpt per book*.
- Cover: the cover is a jpg file that is added as an `attachment` to the Zotero item (see the Zotero attachments [documentation](https://www.zotero.org/support/attaching_files)).