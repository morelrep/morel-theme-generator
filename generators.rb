# Define the command to run the Jekyll server
# jekyll_command = "jekyll build --config _config_local.yml"

# Execute the command and capture its output
#IO.popen(jekyll_command) do |io|
 # io.each do |line|
  #  puts line
  #end
#end

# Define an array of commands
commands = [
  "jekyll build --config _config_local.yml",
  "unzip -d ./assets/ ./_site/assets/env.zip",
  "mkdir ./_site/abouts && cp _includes/site-description.html ./_site/abouts"
]

# Execute each command sequentially
commands.each do |command|
  system(command)
end

