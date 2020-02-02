# Licensed under a 3-clause BSD style license - see LICENSE.rst

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._{{ cookiecutter._parent_project }}_init import *   # noqa
# ----------------------------------------------------------------------------

__all__ = []

{%- if cookiecutter.include_example_code == 'y' %}
from .example_mod import *   # noqa
# Then you can be explicit to control what ends up in the namespace,
__all__ += ['do_primes']   # noqa
# or you can keep everything from the subpackage with the following instead
# __all__ += example_mod.__all__
{%- endif %}
