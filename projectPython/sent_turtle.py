from typing import Iterator


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames: list):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender: str, recipient: str, message_body: str, urgent=False) -> int:
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,

            # Add boolean 'read' key to check whether the user has read the message.
            'read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username: str, number_of_messages=0) -> Iterator[str]:
        """
        Get username and an optional parameter N for the first N messages to read from the inbox
        of the user. If the messages were not read yet, return the messages (the first N messages)
        if the messages were read already return nothing. If the N is not sent or it is bigger than
        the actual number of messages, return all messages in the inbox.

        :param username: The name of the user.
        :param number_of_messages: The number of messages to read from the first message.
        :return: The body of the N first messages that unread (or all the messages in the inbox).
        """
        max_messages = self.boxes[username][-1]['id']
        if not number_of_messages or number_of_messages > max_messages:
            number_of_messages = max_messages
        for i in range(0, number_of_messages):
            if not self.boxes[username][i]['read']:
                self.boxes[username][i]['read'] = True
                yield self.boxes[username][i]['body']

    def search_inbox(self, username: str, sentence: str) -> list[str]:
        """
        Get username and and a string, return list of message that contains the string sent.

        :param username: The name of the user.
        :param sentence: A substring to check if exist in each message
        :return: A list of message that contains the string sent.
        """
        list_messages = [self.boxes[username][i]['body'] for i in range(0, self.boxes[username][-1]['id'])]
        return list(filter(lambda msg: sentence in msg, list_messages))


def show_example():
    """Show example of using the PostOffice class."""

    # Change from tuple to list because PostOffice expect a list and not a tuple
    users = ['Newman', 'Mr. Peanutbutter']
    post_office = PostOffice(users)
    post_office.send_message(
        sender='Mr. Peanutbutter', recipient='Newman', message_body='Hello, Newman.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter', recipient='Newman', message_body='How are you?',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter', recipient='Newman', message_body='Hope you feeling well?',
    )
    print(f"Successfuly sent message number {message_id}.")
    print(post_office.boxes['Newman'])

    print("\nUnread messages:")
    print("**first call (2 first messages):")
    for msg in post_office.read_inbox('Newman', 2):
        print(msg)
    print("**second call (all (3) messages that 2 firsts already read):")
    for msg in post_office.read_inbox('Newman'):
        print(msg)

    print("\nSearch in inbox messages containing 'you':")
    print(post_office.search_inbox('Newman', 'you'))


if __name__ == '__main__':
    show_example()

