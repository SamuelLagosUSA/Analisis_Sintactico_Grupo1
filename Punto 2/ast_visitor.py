from ExpresionesVisitor import ExpresionesVisitor
from ast_nodes import Num, BinOp


class AstBuilder(ExpresionesVisitor):
    def visitE(self, ctx):
        # e : e '+' t | t
        if ctx.getChildCount() == 3:
            return BinOp('+', self.visit(ctx.e()), self.visit(ctx.t()))
        return self.visit(ctx.t())

    def visitT(self, ctx):
        # t : t '*' f | f
        if ctx.getChildCount() == 3:
            return BinOp('*', self.visit(ctx.t()), self.visit(ctx.f()))
        return self.visit(ctx.f())

    def visitF(self, ctx):
        # f : ID | NUM | '(' e ')'
        if ctx.ID():
            return Num(ctx.ID().getText())
        if ctx.NUM():
            return Num(ctx.NUM().getText())
        return self.visit(ctx.e())
