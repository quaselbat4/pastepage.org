package "monit" do
    :upgrade
end

cookbook_file "/etc/monit/monitrc" do
  source "monitrc"
  mode "777"
  owner "root"
  group "root"
end

script "Set monit's startup variable" do
  interpreter "bash"
  user "root"
  group "root"
  code <<-EOH
    echo "startup=1" > /etc/default/monit
  EOH
end

script "Restart monit" do
  interpreter "bash"
  user "root"
  group "root"
  code <<-EOH
    service monit restart
  EOH
end
