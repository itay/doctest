require 'nanoc3/tasks'

task :clean_markdown => [] do
  # Clean the TOC and API generated files
  FileUtils.rm_r('toc') if File.exist?('toc')
  FileUtils.rm_r(File.join('content', 'api')) if File.exist?(File.join('content', 'api'))

  # Create the appropriate directories
  FileUtils.mkdir('toc')
  FileUtils.mkdir(File.join('content', 'api'))
end

desc "Generate Splunk Docs"
task :generate => [] do
  if !ENV["docs"]
    abort "Must supply path to Splunk REST docs directory"
  end

  docs_dir = ENV["docs"]
  cur_dir = File.expand_path(File.dirname(__FILE__))
  
  script = File.join(docs_dir, "genmarkdown.py")

  endpoints_file = File.join(docs_dir, "endpoints.csv")
  groupings_file = File.join(docs_dir, "groupings.txt")
  toc_file = File.join(cur_dir, "toc/toc.html")
  output_dir = File.join(cur_dir, "content/api")

  invocation = "python #{script} --endpoints #{endpoints_file} --groupings #{groupings_file} --toc #{toc_file} --output #{output_dir}"
  Dir.chdir(docs_dir) do
    sh invocation
  end
end

desc "Compile and View Docs"
task :view => [:generate] do
  sh "nanoc compile"
  sh "nanoc view"
end

desc "Publish to Splunk docs"
task :publish => [:clean, :clean_markdown, :generate] do
  FileUtils.rm_r('output') if File.exist?('output')
  
  sh "nanoc compile"

  ENV['GIT_DIR'] = File.expand_path(`git rev-parse --git-dir`.chomp)
  old_sha = `git rev-parse refs/remotes/origin/gh-pages`.chomp
  Dir.chdir('output') do
    ENV['GIT_INDEX_FILE'] = gif = '/tmp/dev.gh.i'
    ENV['GIT_WORK_TREE'] = Dir.pwd
    File.unlink(gif) if File.file?(gif)
    `git add -A`
    tsha = `git write-tree`.strip
    puts "Created tree   #{tsha}"
    if old_sha.size == 40
      csha = `echo 'boom' | git commit-tree #{tsha} -p #{old_sha}`.strip
    else
      csha = `echo 'boom' | git commit-tree #{tsha}`.strip
    end
    puts "Created commit #{csha}"
    puts `git show #{csha} --stat`
    puts "Updating gh-pages from #{old_sha}"
    `git update-ref refs/heads/gh-pages #{csha}`
    `git push origin gh-pages`
  end
end
