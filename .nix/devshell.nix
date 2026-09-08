{
    pkgs,
    perSystem,
    ...
}:
perSystem.devshell.mkShell {
    name = "uni";
    motd = ''
        {141}🏫 uni{reset} shell
        $(type -p menu &>/dev/null && menu)
    '';

    commands = [ ];

    packages = with pkgs; [ ];

    env = [ ];
}
