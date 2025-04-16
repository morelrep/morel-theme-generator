def modify_document(file_path)
   content = File.read(file_path)
 
   modified_content = content.gsub(/^remote_theme:.+$/, "remote_theme: ").gsub(/^podcast:.+$/, "podcast: true")
 
   File.open(file_path, "w") do |file|
     file.puts(modified_content)
   end
 end
 
 # Usage: Call the method with the path of your document file
 modify_document("_config.yml")
 