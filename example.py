from gitlab import Gitlab
GITLAB_SRC='https://gitlab.com'
GITLAB_PROJECT_ID='3472737' # https://gitlab.com/inkscape/inkscape
GITLAB_REF='INKSCAPE_1_0' #https://gitlab.com/inkscape/inkscape/-/tree/INKSCAPE_1_0
PATH_TO_FILE='LICENSES/GPL-2.0.txt'
def main():
    project=Gitlab(GITLAB_SRC).projects.get(GITLAB_PROJECT_ID)
    project.files.get(file_path=PATH_TO_FILE, ref=GITLAB_REF)

if __name__ == '__main__':
    main()