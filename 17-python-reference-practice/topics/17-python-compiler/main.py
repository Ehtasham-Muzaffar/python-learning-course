"""Python compiler: standalone reference and practice project."""

import dis

code = compile("answer = 6 * 7", "<trusted-demo>", "exec")
dis.dis(code)
