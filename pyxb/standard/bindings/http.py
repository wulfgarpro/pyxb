from pyxb.standard.bindings.raw.http import *
import pyxb.standard.bindings.raw.http as raw_http
from pyxb.standard.bindings.wsdl import _WSDL_binding_mixin, _WSDL_port_mixin

class binding (raw_http.binding, _WSDL_binding_mixin):
    pass
raw_http.binding._SetClassRef(binding)

class address (raw_http.address, _WSDL_port_mixin):
    pass
raw_http.address._SetClassRef(address)
