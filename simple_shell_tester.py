import requests
from sys import argv
import os

checker_link = 'https://simple-shell-tests.vercel.app/assets/files/1/2/checker.bash'
task_1_links = ['https://simple-shell-tests.vercel.app/assets/files/1/2/bin_ls.bash', 'https://simple-shell-tests.vercel.app/assets/files/1/3/bin_ls_3_times.bash', 'https://simple-shell-tests.vercel.app/assets/files/1/4/bin_ls_spaces.bash', 'https://simple-shell-tests.vercel.app/assets/files/1/5/ls_in_current_dir.bash', 'https://simple-shell-tests.vercel.app/assets/files/1/6/empty_input_small.bash', 'https://simple-shell-tests.vercel.app/assets/files/1/7/empty_input_large.bash', 'https://simple-shell-tests.vercel.app/assets/files/1/8/empty_input_medium.bash']
task_2_links = ["https://simple-shell-tests.vercel.app/assets/files/2/3/bin_ls_1_arg_1.bash", "https://simple-shell-tests.vercel.app/assets/files/2/2/bin_ls_1_arg.bash", "https://simple-shell-tests.vercel.app/assets/files/2/4/echo_1_arg.bash"]
taks_3_links = ['https://simple-shell-tests.vercel.app/assets/files/3/2/ls_.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/3/ls_in_two_parent_dir_2.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/4/ls_1_arg.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/6/ls_in_parent_dir.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/7/ls_in_two_parent_dir.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/9/bin_ls.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/10/ls_path_bin_last.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/11/bin_ls_large_input.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/12/bin_ls_empty_path.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/13/bin_ls_1_arg.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/14/mix_ls_bin_ls_spaces.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/15/ls_spaces.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/16/ls_empty_path.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/17/bin_ls_spaces.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/18/ls_in_current_dir.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/19/ls_dot_ls.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/20/env_ignore_ls.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/21/ls_path_bin_first.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/22/env_ignore_bin_ls.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/23/bin_ls_3_times.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/24/bin_ls_medium_input.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/25/mix_ls_bin_ls.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/26/ls_path_no_bin.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/27/ls_path_bin_middle.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/28/empty_path_failing_cmd.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/29/path_path1_var.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/30/path_current_dir_ls.bash', 'https://simple-shell-tests.vercel.app/assets/files/3/31/unknown_command_no_fork.bash']
task_4_links = ["https://simple-shell-tests.vercel.app/assets/files/4/3/exit_no_arg_1.bash"]
task_5_links = ['https://simple-shell-tests.vercel.app/assets/files/5/2/env_one_var.bash', 'https://simple-shell-tests.vercel.app/assets/files/5/3/env.bash', 'https://simple-shell-tests.vercel.app/assets/files/5/4/env_ignore_env.bash']
task_6_links = ['https://simple-shell-tests.vercel.app/assets/files/8/2/exit_1000.bash', 'https://simple-shell-tests.vercel.app/assets/files/8/3/exit_with_status.bash', 'https://simple-shell-tests.vercel.app/assets/files/8/4/exit_neg_number.bash', 'https://simple-shell-tests.vercel.app/assets/files/8/5/exit_no_arg_1.bash', 'https://simple-shell-tests.vercel.app/assets/files/8/6/exit_no_arg.bash', 'https://simple-shell-tests.vercel.app/assets/files/8/7/exit_string.bash']
tests = [[], task_1_links, task_2_links, taks_3_links, task_4_links, task_5_links, task_6_links]
mandatory_tests = task_1_links + task_2_links + taks_3_links + task_4_links + task_5_links + task_6_links

def get_user_input():
    while True:
        choice = input("what test would u like to run:\n\
                    1: all the tests\n\
                    2: a single test\n\
                    3: all the tests of a specefic task\n\
                    4: exit\n\
                    -> ")
        try:
            choice = int(choice)
        except:
            print("please enter a numeric value")
            continue
        if (choice not in [1, 2, 3, 4]):
            print("please enter a valid choice")    
            continue
        break
    return choice

def download_test_file(url, dir="."):
    try:
        res = requests.get(url, stream=True)
        if res.status_code == 200:
            file_content = res.content
            file_name = url.split("/")[-1]
            full_path= f"{dir}/{file_name}"
            with open(full_path, 'wb') as f:
                f.write(file_content)
            print(f"{file_name} downloaded successfully")
        else:
            print("could not open the link")
    except requests.RequestException as e:
        print("An error occurred:", e)

def run_single_test(task_number, test_number, tests_dir):
    link = tests[task_number][test_number]
    file_name = link.split("/")[-1]
    full_path = f"{tests_dir}/{file_name}"
    cmd = f"./{tests_dir}/checker.bash ./hsh {full_path}"
    print(f"{file_name}: ")
    os.system(cmd)
    print()

def run_tests(tests, tests_dir):
    for link in tests:
        file_name = link.split("/")[-1]
        full_path = f"{tests_dir}/{file_name}"
        cmd = f"./{tests_dir}/checker.bash ./hsh {full_path}"
        print(f"{file_name}: ")
        os.system(cmd)
        print()

def download_test_files(links, dir_name):
    for link in links:
        download_test_file(link, dir_name)


def main():
    dir_name = "simple_shell_tests"
    if len(argv) != 2:
        print(f"Usage: python3 {__file__} [d | download | t | test]")
        print("download: download the mandatory tests")
        print("start the testing")
        exit(1)
    to_do = argv[1].lower()
    if to_do == "d" or to_do == "download":
        if (not os.path.exists(dir_name)):
            os.makedirs(dir_name)
        download_test_file(checker_link, dir_name)
        os.chmod(f"{dir_name}/checker.bash", 0o777)
        download_test_files(mandatory_tests, dir_name)
    elif to_do == "t" or to_do == "test":
        if (not os.path.exists(dir_name)):
            print("simple_shell_tests directory doesn't exist")
            exit(1)
        choice = get_user_input()
        if choice == 1:
            run_tests(mandatory_tests, dir_name)
        elif choice == 2:
            while True:
                try:
                    task_number = int(input("enter the task number: "))
                    test_number = int(input("enter the test number: "))
                except:
                    print(f"please provide integer numbers ")
                    continue
                if (task_number == 0):
                    print("the holly betty should be checked manully")
                    return
                if (task_number < 0 or task_number >= len(tests)):
                    print(f"please provide a valid task number [0, {len(tests) - 1}]")
                    continue
                if (test_number < 0 or  test_number >= len(tests[task_number])):
                    print(f"please provide a valid test number [0, {len(tests[task_number]) - 1}]")
                    continue
                break
            run_single_test(task_number, test_number, dir_name)
        elif choice == 3:
            while True:
                try:
                    task_number = int(input("enter the task number: "))
                except:
                    print("please enter a numeric number")
                    continue
                if task_number < 0 or task_number >= len(tests):
                    print(f"please enter a valid task number [0, {len(tests) - 1}]")
                    continue
                break
            if task_number == 0:
                print("the holly betty should be tested manually")
            else:
                run_tests(tests[task_number], dir_name)
        elif choice == 4:
            exit(0)
    else:
        print("invalid choice")

if __name__ == "__main__":
    main()
