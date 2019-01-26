def test_file_discriptor_exist(host):
    assert host.file("/etc/security/limits.conf").contains("root soft nofile 65536")
    assert host.file("/etc/security/limits.conf").contains("root hard nofile 65536")
    assert host.file("/etc/security/limits.conf").contains("* soft nofile 65536")
    assert host.file("/etc/security/limits.conf").contains("* hard nofile 65536")

def test_ntp_is_installed(host):
    ntp = host.package("ntp")
    assert ntp.is_installed
    assert ntp.version.startswith("1:4.2.8p4+dfsg-3ubuntu5.7")

def test_ntp_running_and_enabled(host):
    ntp = host.service("ntp")
    assert ntp.is_running
    assert ntp.is_enabled

def test_ntp_port_enabled(host):
    assert host.socket("udp://0.0.0.0:123").is_listening

def test_ntp_setting_exist(host):
    assert host.file("/etc/ntp.conf").contains("server ntp1.jst.mfeed.ad.jp iburst")
    assert host.file("/etc/ntp.conf").contains("server ntp2.jst.mfeed.ad.jp iburst")
    assert host.file("/etc/ntp.conf").contains("server ntp3.jst.mfeed.ad.jp iburst")

def test_ntpdate_is_installed(host):
    ntpdate = host.package("ntpdate")
    assert ntpdate.is_installed
    assert ntpdate.version.startswith("4.2.8p4@1.3265-o")

def test_apt_setting_exist(host):
    assert host.file("/etc/apt/apt.conf.d/20auto-upgrades").contains("APT::Periodic::Update-Package-Lists \"0\";")
    assert host.file("/etc/apt/apt.conf.d/20auto-upgrades").contains("APT::Periodic::Unattended-Upgrade \"0\";")

def test_bind_is_installed(host):
    nginx = host.package("bind9")
    assert nginx.is_installed
    assert nginx.version.startswith("1:9.10.3.dfsg.P4-8ubuntu1.8")

def test_bind_running_and_enabled(host):
    nginx = host.service("bind9")
    assert nginx.is_running
    assert nginx.is_enabled
