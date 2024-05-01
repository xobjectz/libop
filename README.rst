NAME

::

    LIBOP - original programmer


SYNOPSIS

::

    op <cmd> [key=val] [key==val]
    op [-a] [-c] [-d] [-h] [-v]

    options are:

    -a     load all modules
    -c     start console
    -d     start daemon
    -h     display help
    -v     use verbose


INSTALL

::

    $ pipx install libop
    $ pipx ensurepath


DESCRIPTION

::

    LIBOP is a bot runtime, it provides a runtime on which bots can run.

    LIBOP contains all the python3 code to program objects in a functional
    way. It provides a base Object class that has only dunder methods, all
    methods are factored out into functions with the objects as the first
    argument. It is called Object Programming (OP), OOP without the
    oriented.

    LIBOP allows for easy json save//load to/from disk of objects. It
    provides an "clean namespace" Object class that only has dunder
    methods, so the namespace is not cluttered with method names. This
    makes storing and reading to/from json possible.

    LIBOP has all you need to program a unix cli program, such as disk
    perisistence for configuration files, event handler to handle the
    client/server connection, code to introspect modules for
    commands, deferred exception handling to not crash on an error, a
    parser to parse commandline options and values, etc.

    LIBOP has a demo bot, it can connect to IRC, fetch and display RSS
    feeds, take todo notes, keep a shopping list and log text. You can
    also copy/paste the service file and run it under systemd for 24/7
    presence in a IRC channel.

    LIBOP is Public Domain.


CONFIGURATION

::

    $ op cfg 
    channel=#op commands=True nick=op port=6667 server=localhost

    irc

    $ op cfg server=<server>
    $ op cfg channel=<channel>
    $ op cfg nick=<nick>

    sasl

    $ op pwd <nsvnick> <nspass>
    $ op cfg password=<frompwd>

    rss

    $ op rss <url>
    $ op dpl <url> <item1,item2>
    $ op rem <url>
    $ op nme <url> <name>


USAGE

::

    without any argument the program does nothing

    $ op
    $

    see list of commands

    $ op cmd
    cmd,err,mod,req,thr,ver

    list of modules

    $ op mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr

    use -c to start a console

    $ op -c

    use mod=<name1,name2> to load additional modules

    $ op -c mod=irc,rss
    >

    use -v for verbose

    $ op -cv mod=irc
    OP started CV started Sat Dec 2 17:53:24 2023
    >


COMMANDS

::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    fnd - find objects 
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed
    thr - show the running threads

SYSTEMD

::

    save the following it in /etc/systemd/system/op.service and
    replace "<user>" with the user running pipx

    [Unit]
    Description=original programmer
    Requires=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.op
    ExecStart=/home/<user>/.local/pipx/venvs/op/bin/op -d
    RemainAfterExit=yes

    [Install]
    WantedBy=default.target

    then run this

    $ mkdir ~/.op
    $ sudo systemctl enable op --now

    default channel/server is #op on localhost

FILES

::

    ~/.op
    ~/.local/bin/op
    ~/.local/pipx/venvs/op/

AUTHOR

::

    xobjectz objx@proton.me>

COPYRIGHT

::

    LIBOP is Public Domain.
