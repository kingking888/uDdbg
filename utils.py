import inquirer
from termcolor import colored
from unicorn import *


def error_format(command, text):
    return colored("ERR", 'red', attrs=['bold', 'underline']) + "(" + colored(command, 'white', attrs=['bold', 'underline']) + "): " + text

def input_to_offset(off):
    try:
        if off.startswith('0x'):
            return int(off, 16)
        else:
            return int(off)
    except Exception as e:
        raise Exception('Invalid integer')


def white_bold(text):
    return colored(text, attrs=['bold', 'dark'])


def white_bold_underline(text):
    return colored(text, attrs=['dark', 'bold', 'underline'])


def green_bold(text):
    return colored(text, 'green', attrs=['bold', 'dark'])


def red_bold(text):
    return colored(text, 'red', attrs=['bold', 'dark'])


def get_arch_consts(arch):
    if arch == UC_ARCH_ARM:
        return arm_const
    elif arch == UC_ARCH_ARM64:
        return arm64_const
    elif arch == UC_ARCH_M68K:
        return m68k_const
    elif arch == UC_ARCH_MIPS:
        return mips_const
    elif arch == UC_ARCH_SPARC:
        return sparc_const
    elif arch == UC_ARCH_X86:
        return x86_const


def get_reg_tag(arch):
    if arch == UC_ARCH_ARM:
        return "UC_ARM_REG_"
    elif arch == UC_ARCH_ARM64:
        return "UC_ARM64_REG_"
    elif arch == UC_ARCH_M68K:
        return "UC_M68K_REG_"
    elif arch == UC_ARCH_MIPS:
        return "UC_MIPS_REG_"
    elif arch == UC_ARCH_SPARC:
        return "UC_SPARC_REG_"
    elif arch == UC_ARCH_X86:
        return "UC_X86_REG_"


def prompt_list(items, key, hint):
    base_path = [
        inquirer.List(key,
                      message=hint,
                      choices=items)]
    r = inquirer.prompt(base_path)
    return r[key]
