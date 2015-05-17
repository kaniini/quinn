# Quinn: an enhanced version of nano for powerusers

Quinn is an enhanced fork of nano with the goals of reducing wasted space
by the user interface.  Visually it looks similar to vim, but maintains the
modeless editing style of nano.

## License status

It is based on GNU nano 2.4.1, which is under the GPLv3 license.  The
*modifications* that we have made should be considered however to be either
public domain, or in the absence of a public domain, placed under the ISC
license.  Alternatively you can use the modifications under the GPLv3 license,
but we have no plans to assign copyright on them over to FSF.

Incidentally, in typical GNU style, Quinn is a "recursive acronym" which expands to
"Quinn Universally Is Not Nano."  The authors wish to strongly reminder the reader,
however, that Quinn is not affiliated with the GNU project in any way.

## Building and installing Quinn

    $ tar zxvf nano-x.y.z.tar.gz
    $ cd nano-x.y.z
    $ ./configure
    $ make
    $ sudo make install

It's that simple.  Use --prefix with configure to override the
default installation directory of /usr/local.

If you haven't configured with the `--disable-nanorc` option, after
installation you may want to copy the doc/nanorc.sample to your
home directory, rename it to `.nanorc`, and then edit it according
to your taste.

## Wait.  Why does Quinn read my `.nanorc`?

Quinn is backwards compatible with nano.  In this case, this means that
it will use your syntax highlighting and (some) configuration choices
from your `.nanorc` file.  However, we strongly suggest using the syntax
highlighting settings from Quinn; they are much better and take full
advantage of Quinn's syntax highlighting engine.

## Web Page, Contact, Etc.

See our [GitHub](http://github.com/kaniini/quinn).
