def reverse_document(file_path, new_remote_theme)
  content = File.read(file_path)

  modified_content = content.gsub(/^remote_theme:(.*\n)/, "remote_theme: #{new_remote_theme}\n")

  File.open(file_path, "w") do |file|
    file.puts(modified_content)
  end
end

# Usage: Call the method with the path of your document file and the new remote_theme value
reverse_document("_config.yml", "morelrep/morel-theme")
