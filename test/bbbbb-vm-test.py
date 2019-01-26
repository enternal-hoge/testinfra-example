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

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.10.3-0ubuntu0.16.04.2")

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_nginx_port_enabled(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening

def test_squid_is_installed(host):
    nginx = host.package("squid")
    assert nginx.is_installed
    assert nginx.version.startswith("3.5.12-1ubuntu7.4")

def test_squid_running_and_enabled(host):
    nginx = host.service("squid")
    assert nginx.is_running
    assert nginx.is_enabled

def test_squid_port_enabled(host):
    assert host.socket("tcp://0.0.0.0:3128").is_listening