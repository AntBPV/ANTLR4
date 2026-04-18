from WhileLangVisitor import WhileLangVisitor

# Excepciones para control de flujo
class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass


class VisitorImpl(WhileLangVisitor):

    def __init__(self):
        self.memory_stack = [{}]
        self.type_stack = [{}]

    def enterScope(self):
        self.memory_stack.append({})
        self.type_stack.append({})

    def exitScope(self):
        self.memory_stack.pop()
        self.type_stack.pop()

    def currentMemory(self):
        return self.memory_stack[-1]

    def currentTypes(self):
        return self.type_stack[-1]

    def findVariable(self, name):
        for scope in reversed(self.type_stack):
            if name in scope:
                return scope[name]
        return None

    def setVariable(self, name, value):
        for scope in reversed(self.memory_stack):
            if name in scope:
                scope[name] = value
                return
        raise Exception(f"Variable '{name}' no declarada")

    # program: statement+ EOF;
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        var_type = ctx.TYPE().getText()

        if var_name in self.currentTypes():
            raise Exception(f"Variable '{var_name}' ya fue declarada en este ámbito")

        value = self.visit(ctx.expr())

        self.currentMemory()[var_name] = value
        self.currentTypes()[var_name] = var_type

    # assignment: ID ASSIGN expr SEMI;
    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()

        var_type = self.findVariable(var_name)

        if var_type is None:
            raise Exception(f"Variable '{var_name}' no declarada")

        value = self.visit(ctx.expr())

        if isinstance(value, int):
            value_type = "int"
        elif isinstance(value, str):
            value_type = "string"
        else:
            raise Exception("Tipo desconocido")

        if var_type != value_type:
            raise Exception(
                f"Error de tipo: no se puede asignar {value_type} a {var_type}"
            )

        self.setVariable(var_name, value)

    def visitStringExpr(self, ctx):
        return ctx.STRING().getText().strip('"')

    # expr
    def visitArithmeticExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.OP().getText()

        if op == '+':
            if isinstance(left, int) and isinstance(right, int):
                return left + right
            if isinstance(left, str) and isinstance(right, str):
                return left + right
            raise Exception("Operación '+' inválida entre tipos diferentes")

        if not isinstance(left, int) or not isinstance(right, int):
            raise Exception("Operación aritmética inválida: solo se permiten enteros")

        if op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left // right

    def visitComparisonExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.operator().getText()

        if op in ['<', '>']:
            if not isinstance(left, int) or not isinstance(right, int):
                raise Exception("Comparación inválida: solo se permiten enteros con < o >")

            return left < right if op == '<' else left > right

        if op == '==':
            return left == right
        elif op == '!=':
            return left != right

    def visitIdExpr(self, ctx):
        var_name = ctx.ID().getText()

        for scope in reversed(self.memory_stack):
            if var_name in scope:
                return scope[var_name]

        raise Exception(f"Variable '{var_name}' no declarada")

    def visitNumberExpr(self, ctx):
        return int(ctx.NUMBER().getText())

    # condition: expr;
    def visitCondition(self, ctx):
        value = self.visit(ctx.expr())

        if not isinstance(value, bool):
            raise Exception("Condición inválida: la expresión no es booleana")

        return value

    # whileStatement
    def visitWhileStatement(self, ctx):
        while True:
            condition_value = self.visit(ctx.condition())

            if not isinstance(condition_value, bool):
                raise Exception("Condición inválida en while")

            if not condition_value:
                break

            self.enterScope()

            try:
                for stmt in ctx.statement():
                    self.visit(stmt)

            except ContinueException:
                self.exitScope()
                continue

            except BreakException:
                self.exitScope()
                break

            self.exitScope()

    # ifStatement
    def visitIfStatement(self, ctx):
        condition_value = self.visit(ctx.condition())

        if not isinstance(condition_value, bool):
            raise Exception("Condición inválida en if")

        statements = ctx.statement()

        if ctx.ELSE():
            split = len(statements) // 2
            then_block = statements[:split]
            else_block = statements[split:]
        else:
            then_block = statements
            else_block = []

        if condition_value:
            self.enterScope()
            for stmt in then_block:
                self.visit(stmt)
            self.exitScope()

        else:
            if else_block:
                self.enterScope()
                for stmt in else_block:
                    self.visit(stmt)
                self.exitScope()

    # break;
    def visitBreakStatement(self, ctx):
        raise BreakException()

    # continue;
    def visitContinueStatement(self, ctx):
        raise ContinueException()