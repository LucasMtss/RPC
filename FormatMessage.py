def encode_message(operacao, args):
    response = operacao + '#'
    response += '#'.join([str(x) for x in args])
    return response