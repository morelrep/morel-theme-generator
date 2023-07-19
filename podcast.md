---
title: MOREL
tagline: News on Mobile Open Resilient Electronic Libraries
layout: post-index
---
<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <div class="ficha-metadata">
          Aired on <span class="metadata-input">{{ post.date | date_to_string }}</span> with <span class="metadata-input">{{ post.guest }}</span><!-- here we will add tags that associate podcast episodes with content on the archive-->        
      </div>
    </li>
  {% endfor %}
</ul>