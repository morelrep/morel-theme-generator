# Define the command to run the Jekyll server
jekyll_command = "bundle exec jekyll serve --config _config.yml,_config_local.yml --livereload --baseurl '/morel-theme-generator'"

# Execute the command and capture its output
IO.popen(jekyll_command) do |io|
  io.each do |line|
    puts line
  end
end
