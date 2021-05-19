class Solution:
    def findDuplicate(self,paths):
        """
        :param paths:
        :return: List[List[str]]
        """
        contents = defaultdict(list)

        for path in paths:
            path = path.split(" ")
            prefix = path[0]

            pattern1 = r"\(.+\)$"
            pattern = r"\("
            for file in path[1:]:
                # 1.txt(abcd) - search pattern
                res = re.split(pattern,file)
                file_name = res[0]
                file_content = res[1][:-1]
                full_file_path = prefix + "/" + file_name

                contents[file_content].append(full_file_path)
        ans = []
        for v in contents.values():
            if len(v) >= 2:
                ans.append(v)

        return ans
