---
title: description
lang: en
---
MOREL generates web sites from bibliographic collections. The MOREL sites gather book covers, excerpts, bibliographic clues, metadata and digital downloads from works stored in the Zotero reference manager.

<!-- more -->

Works are organized by dynamic lists, which automatically group the works according to common characteristics:

- [authors]({{site.BASE_PATH}}/criteria/author)
- [city of publication]({{site.BASE_PATH}}/criteria/city)
- [imprint or publisher]({{site.BASE_PATH}}/criteria/publisher)
- [nationality of authors]({{site.BASE_PATH}}/criteria/nationality)
- [edition date]({{site.BASE_PATH}}/criteria/edition)
- [digital repository]({{site.BASE_PATH}}/criteria/repository).

MOREL also has a [search engine]({{site.BASE_PATH}}/search) that allows you to find works directly.

# Installation Instructions

## Prerequisites

- **Zotero**: Install Zotero reference management software from the [official website](https://www.zotero.org/) and create collections to organize your content.

- **Python**: Install Python programming language from the [official Python website](https://www.python.org/) based on your operating system. Ensure you have Python version 3.x installed.

- **Jekyll**: Install Jekyll, a static site generator, using your preferred method:
  - For macOS or Linux, open a terminal and run the following command:
    ```bash
    $ gem install bundler jekyll
    ```
  - For Windows, follow the installation guide provided on the [Jekyll website](https://jekyllrb.com/docs/installation/windows/).

## Installation Steps

1. **Download the Web Site Generator**

   - Visit the GitHub repository for the web site generator at [https://github.com/example/repository](https://github.com/example/repository).
   - Click on the "Download" button or clone the repository using the following command:
     ```bash
     $ git clone https://github.com/example/repository.git
     ```

2. **Configure Jekyll**

   - Open a terminal and navigate to the downloaded repository's directory:
     ```bash
     $ cd /path/to/repository
     ```
   - Install the necessary dependencies by running:
     ```bash
     $ bundle install
     ```
   - Customize the Jekyll configuration file (`_config.yml`) to match your preferences and set up necessary plugins or themes.

3. **Run Python Scripts**

   - Ensure that you have Python installed and accessible from the command line.
   - Navigate to the `scripts` directory within the downloaded repository:
     ```bash
     $ cd /path/to/repository/scripts
     ```
   - Execute the Python script(s) provided in the repository to extract data from your Zotero collections. For example:
     ```bash
     $ python extract_data.py
     ```
   - Follow any prompts or instructions provided by the script(s).

4. **Generate the Website**

   - Return to the main directory of the downloaded repository:
     ```bash
     $ cd /path/to/repository
     ```
   - Build the website using Jekyll by running the following command:
     ```bash
     $ bundle exec jekyll build
     ```
   - Once the build process completes, the generated website will be available in the `_site` directory.

5. **Deployment**

   - Deploy the generated website to your desired web server or hosting platform by following their respective instructions.



## "About" page for your site

If you aren't using MOREL yet, go to the [installation instructions](#install) bellow. If you installed MOREL already, these are your last steps to have it ready to run:

- Delete the file `_abouts/site-description.md`
- Edit `site-description_template`. Note that `site-description-template.md` has the current description for one of the sites built with MOREL: Afro-Latin American Writers in Translation (ALAWiT). Edit to your site's needs. But that there are dynamic fields, such as "{{ site.title }}" and "{{ site.books.size }}". We recommend you to keep them in your edition, so your site description is automatically updated as your collection grows.
- Rename the file to `site description.md`
- Run Jekyll build if you are using a local server, or wait for Github to deploy



