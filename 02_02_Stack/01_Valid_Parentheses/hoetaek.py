class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == ")":
                if st and st[-1] == "(":
                    st.pop()
                else:
                    st.append(i)
            elif i == "]":
                if st and st[-1] == "[":
                    st.pop()
                else:
                    st.append(i)
            elif i == "}":
                if st and st[-1] == "{":
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)
        return not st
