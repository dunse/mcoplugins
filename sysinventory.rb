begin
  require 'rpm'
rescue LoadError
  # we have a failback option anyway
  nil
end

module MCollective
    module Agent
        class Sysinventory<RPC::Agent
            metadata :name        => "Get inventory information from the OS",
                     :description => "Inventory of packages, etc.",
                     :author      => "Louis Coilliot",
                     :license     => "GPLv3",
                     :version     => "0.1",
                     :url         => "",
                     :timeout     => 60

            action "rpmlist" do
              rpmlist = []

              if Gem.available?('ruby-rpm')
                # I love APIs and gems !
                @db = RPM::DB.new.each do |pkg|
                    rpmlist << { 'name' => pkg.name,
                                 'version' => pkg.version.v,
                                 'release' => pkg.version.r,
                                 'architecture' => pkg.arch,
                                 'epoch' => pkg.version.e }
                end

              else
                # I prefer running a shell command !
                keys = ['name','version','release','architecture','epoch']
                rpmqa = `rpm -qa --qf '%{NAME}:%{VERSION}:%{RELEASE}:%{ARCH}:%{EPOCH}\n'`
                rpmqa.each do |line|
                  vals = line.chomp.split(':')
                  rpmlist << keys.zip(vals).inject({}){|h,e| h[e[0]] = e[1]; h}
                end
              end

              reply["rpmlist"] = rpmlist
            end
        end
    end
end