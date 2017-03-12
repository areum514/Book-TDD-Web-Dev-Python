#!/usr/bin/env python3
import unittest

from book_tester import ChapterTest


class Chapter19Test(ChapterTest):
    chapter_name = 'chapter_outside_in'
    previous_chapter = 'chapter_server_side_debugging'

    def test_listings_and_commands_and_output(self):
        self.parse_listings()
        #self.prep_virtualenv()

        # sanity checks
        self.assertEqual(self.listings[0].type, 'code listing with git ref')
        self.assertEqual(self.listings[1].type, 'code listing with git ref')
        self.assertEqual(self.listings[2].type, 'code listing currentcontents')

        # skips
        #self.skip_with_check(22, 'switch back to master') # comment

        self.start_with_checkout()
        self.prep_database()

        # hack fast-forward
        skip = False
        if skip:
            self.pos = 53
            self.sourcetree.run_command('git checkout {}'.format(
                self.sourcetree.get_commit_spec('ch19l025')
            ))

        while self.pos < len(self.listings):
            print(self.pos, self.listings[self.pos].type)
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)
        self.check_final_diff(ignore=["moves", "Generated by Django 1.11"])


if __name__ == '__main__':
    unittest.main()
