Summary:	Plasma desktop configuration
Name:		distro-plasma-config
Version:	0.6
Release:	16
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		%{disturl}
Source0:	kcmdisplayrc
Source1:	kcmfonts
Source2:	kcminputrc
Source3:	kdeglobals
Source4:	kscreenlockerrc
Source5:	ksplashrc
Source6:	kwinrc
Source7:	metadata.desktop
Source8:	org.kde.plasma.desktop-layout.js
Source9:	org.openmandriva.plasma.desktop.defaultPanel-layout.js
Source10:	plasmarc
Source11:	startupconfig
Source12:	startupconfigfiles
Source13:	startupconfigkeys
Source14:	plasma-firstsetup.sh
Source16:	kcm-about-distrorc
Source17:	ksmserverrc
Source18:	kiorc
Source19:	dolphinrc
Source21:	Sonnet.conf
Source22:	konsolerc
Source23:	klaunchrc
Source24:	discoverabstractnotifier.notifyrc
Source25:	plasma_workspace.notifyrc
Source26:	kdeglobals.sh
Source27:	powermanagementprofilesrc
# Alternative config to make Crapple converts feel at home
Source50:	org.openmandriva.plasma.desktop.globalMenuPanel-layout.js
Source51:	metadata-globalMenu.desktop

# (tpg) disable debug in Qt5 apps
Source100:	qtlogging.ini
Source101:	OMV.profile
BuildRequires:	cmake(ECM)
Requires:	distro-theme >= 1.4.41-4
Requires:	breeze
Requires:	breeze-gtk
Requires:	breeze-icons
Requires:	noto-sans-fonts
Requires(post,postun): pam
Provides:	kde4-config-file
Provides:	distro-kde4-config-OpenMandriva = 2015.0
Provides:	distro-kde4-config-OpenMandriva-common = 2015.0
Obsoletes:	distro-kde4-config-OpenMandriva < 2015.0
Obsoletes:	distro-kde4-config-OpenMandriva-common < 2015.0
Provides:	mandriva-kde4-config = 2014.0
Obsoletes:	mandriva-kde4-config < 2014.0
Provides:	distro-kde4-config-common = 2015.0
Obsoletes:	distro-kde4-config-common < 2015.0
BuildArch:	noarch

%description
Plasma desktop configuration.

%prep

%build

%install
mkdir -p %{buildroot}%{_kde5_sysconfdir}/xdg
mkdir -p %{buildroot}%{_kde5_sysconfdir}/xdg/KDE
mkdir -p %{buildroot}%{_kde5_sysconfdir}/xdg/QtProject
mkdir -p %{buildroot}%{_kde5_sysconfdir}/xdg/plasma-workspace/env
mkdir -p %{buildroot}%{_kde5_sysconfdir}/xdg/plasma-workspace/shutdown
mkdir -p %{buildroot}%{_kde5_datadir}/kservices5
mkdir -p %{buildroot}%{_kde5_datadir}/plasma/shells/org.kde.plasma.desktop/contents
mkdir -p %{buildroot}%{_kde5_datadir}/plasma/layout-templates/org.openmandriva.plasma.desktop.defaultPanel/contents
mkdir -p %{buildroot}%{_datadir}/konsole
install -m 0644 %{SOURCE0} %{buildroot}%{_kde5_sysconfdir}/xdg/kcmdisplayrc
install -m 0644 %{SOURCE1} %{buildroot}%{_kde5_sysconfdir}/xdg/kcmfonts
install -m 0644 %{SOURCE2} %{buildroot}%{_kde5_sysconfdir}/xdg/kcminputrc
install -m 0644 %{SOURCE3} %{buildroot}%{_kde5_sysconfdir}/xdg/kdeglobals
install -m 0644 %{SOURCE4} %{buildroot}%{_kde5_sysconfdir}/xdg/kscreenlockerrc
install -m 0644 %{SOURCE5} %{buildroot}%{_kde5_sysconfdir}/xdg/ksplashrc
install -m 0644 %{SOURCE6} %{buildroot}%{_kde5_sysconfdir}/xdg/kwinrc
install -m 0644 %{SOURCE7} %{buildroot}%{_kde5_datadir}/plasma/layout-templates/org.openmandriva.plasma.desktop.defaultPanel/metadata.desktop
install -m 0644 %{SOURCE7} %{buildroot}%{_kde5_datadir}/kservices5/plasma-layout-template-org.openmandriva.plasma.desktop.defaultPanel.desktop
install -m 0644 %{SOURCE8} %{buildroot}%{_kde5_datadir}/plasma/shells/org.kde.plasma.desktop/contents/layout.js
install -m 0644 %{SOURCE9} %{buildroot}%{_kde5_datadir}/plasma/layout-templates/org.openmandriva.plasma.desktop.defaultPanel/contents/layout.js
install -m 0644 %{SOURCE10} %{buildroot}%{_kde5_sysconfdir}/xdg/plasmarc
install -m 0644 %{SOURCE11} %{buildroot}%{_kde5_sysconfdir}/xdg/startupconfig
install -m 0644 %{SOURCE12} %{buildroot}%{_kde5_sysconfdir}/xdg/startupconfigfiles
install -m 0644 %{SOURCE13} %{buildroot}%{_kde5_sysconfdir}/xdg/startupconfigkeys
install -m 0644 %{SOURCE14} %{buildroot}%{_kde5_sysconfdir}/xdg/plasma-workspace/env/plasma-firstsetup.sh
install -m 0644 %{SOURCE16} %{buildroot}%{_kde5_sysconfdir}/xdg/kcm-about-distrorc
install -m 0644 %{SOURCE17} %{buildroot}%{_kde5_sysconfdir}/xdg/ksmserverrc
install -m 0644 %{SOURCE18} %{buildroot}%{_kde5_sysconfdir}/xdg/kiorc
install -m 0644 %{SOURCE19} %{buildroot}%{_kde5_sysconfdir}/xdg/dolphinrc
install -m 0644 %{SOURCE21} %{buildroot}%{_kde5_sysconfdir}/xdg/KDE/Sonnet.conf
install -m 0644 %{SOURCE22} %{buildroot}%{_kde5_sysconfdir}/xdg/konsolerc
install -m 0644 %{SOURCE23} %{buildroot}%{_kde5_sysconfdir}/xdg/klaunchrc
install -m 0644 %{SOURCE24} %{buildroot}%{_kde5_sysconfdir}/xdg/discoverabstractnotifier.notifyrc
install -m 0644 %{SOURCE25} %{buildroot}%{_kde5_sysconfdir}/xdg/plasma_workspace.notifyrc
install -m 0644 %{SOURCE26} %{buildroot}%{_kde5_sysconfdir}/xdg/plasma-workspace/env/kdeglobals.sh
install -m 0644 %{SOURCE27} %{buildroot}%{_kde5_sysconfdir}/xdg/powermanagementprofilesrc

install -m 0644 %{SOURCE100} %{buildroot}%{_kde5_sysconfdir}/xdg/QtProject/qtlogging.ini
install -m 0644 %{SOURCE101} %{buildroot}%{_datadir}/konsole/OMV.profile

mkdir -p %{buildroot}%{_kde5_datadir}/plasma/layout-templates/org.openmandriva.plasma.desktop.globalMenuPanel/contents
install -m 0644 %{S:50} %{buildroot}%{_kde5_datadir}/plasma/layout-templates/org.openmandriva.plasma.desktop.globalMenuPanel/contents/layout.js
install -m 0644 %{S:51} %{buildroot}%{_kde5_datadir}/plasma/layout-templates/org.openmandriva.plasma.desktop.globalMenuPanel/metadata.desktop

%post
# dont set theme here as it forces it over whatever the user has in ~/.config/gtk-3.0/settings.ini
if grep -q "GTK_THEME=Breeze" %{_sysconfdir}/environment ; then
    sed -i -e "s/^GTK_THEME=Breeze//g" %{_sysconfdir}/environment
fi

%postun
if [ $1 -eq 0 ] ; then
    if grep -q "GTK_THEME=Breeze" %{_sysconfdir}/environment ; then
	sed -i -e "s/^GTK_THEME=Breeze//g" %{_sysconfdir}/environment
    fi
fi

%files
%{_kde5_sysconfdir}/xdg/*
%{_datadir}/konsole/OMV.profile
%{_kde5_datadir}/kservices5/plasma-layout-template-org.openmandriva.plasma.desktop.defaultPanel.desktop
%{_kde5_datadir}/plasma/layout-templates/org.openmandriva.plasma.desktop.defaultPanel
%{_kde5_datadir}/plasma/shells/org.kde.plasma.desktop/contents/layout.js

%{_datadir}/plasma/layout-templates/org.openmandriva.plasma.desktop.globalMenuPanel
