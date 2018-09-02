class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''
         1 = ()
         2 = [(()), () (),]
         3 = [(() ()) , ((())), (()) (), () () (), () (()) ]
        '''
        def gen_paren(n, s="", results=[], open_=0, close=0):
            if len(s) == 2*n:
                results.append(s)
                return 
            if open_ < n:
                gen_paren(n, s+"(", results, open_+1, close)
                        
            if close < open_:
                gen_paren(n, s+")", results, open_, close+1)
            return results
        return gen_paren(n, "", [], 0, 0)
