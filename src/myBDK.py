#!/usr/bin/env python3
# import asyncio
# import logging.config
import html.parser
from pathlib import Path

# from symphony.bdk.core.activity.command import CommandContext
from symphony.bdk.core.config.loader import BdkConfigLoader
# from symphony.bdk.core.service.datafeed.real_time_event_listener import RealTimeEventListener
from symphony.bdk.core.symphony_bdk import SymphonyBdk
# from symphony.bdk.gen.agent_model.v4_initiator import V4Initiator
# from symphony.bdk.gen.agent_model.v4_message_sent import V4MessageSent

# from .activities import EchoCommandActivity, GreetUserJoinedActivity
# from .gif_activities import GifSlashCommand, GifFormReplyActivity
import html
from typing import IO, TextIO, BinaryIO
# Configure logging
current_dir = Path(__file__).parent.parent
# logging_conf = Path.joinpath(current_dir, 'resources', 'logging.conf')
# logging.config.fileConfig(logging_conf, disable_existing_loggers=False)
#streamIdTestRoom = "wsXxwGntMFd87PnnKbcbu3___nCDx_PodA"


async def run_bdk(msg:str,streamId:str,file_to_send:IO = None):
    config = BdkConfigLoader.load_from_file(Path.joinpath(current_dir, 'resources', 'config.yaml'))

    async with SymphonyBdk(config) as bdk:
        # datafeed_loop = bdk.datafeed()
        # datafeed_loop.subscribe(MessageListener())

        # activities = bdk.activities()
        # activities.register(EchoCommandActivity(bdk.messages()))
        # activities.register(GreetUserJoinedActivity(bdk.messages(), bdk.users()))
        # activities.register(GifSlashCommand(bdk.messages()))
        # activities.register(GifFormReplyActivity(bdk.messages()))

        # streamId = "wsXxwGntMFd87PnnKbcbu3___nCDx_PodA"
        msgString = f"<messageML>{msg}</messageML>"
        await bdk.messages().send_message(streamId, msgString,attachment=[file_to_send])
        # @activities.slash("/hello")
        # async def hello(context: CommandContext):
        #     name = context.initiator.user.display_name
        #     response = f"<messageML>Hello {name}, {context.stream_id} hope you are doing well!</messageML>"
        #     await bdk.messages().send_message(context.stream_id, response)

        # Start the datafeed read loop
        # await datafeed_loop.start()
        # streamId = "wsXxwGntMFd87PnnKbcbu3___nCDx_PodA"
        # msgString = f"<messageML>Hello Patrick hope you are doing well!</messageML>"
        # await bdk.messages().send_message(streamId, msgString)

# class MessageListener(RealTimeEventListener):
#     async def on_message_sent(self, initiator: V4Initiator, event: V4MessageSent):
#         logging.debug("Message received from %s: %s",
#             initiator.user.display_name, event.message.message)

class UtilsMethods:
    def __init__(self) -> None:
        pass
        #self.specialCharDict = {'<':'&lt;', '&':'&#38;','$':'&#36;', '#':'&#35;','>':'&gt;','"':'&quot;',"'":"&#39;",'*':'&#42;','%':'&#37;'}
        
    def text_parser(self, text: str) -> str:
        text = html.escape(text)
        text = text.replace('\n','<br/>')
        return text
    
    # (Below is my own initial text parser that tries to escape html special characters)
    # def text_parser(self, text: str) -> str:
    # #specialCharDict = {'<':'&lt;', '&':'&#38;','$':'&#36;', '#':'&#35;','>':'&gt;','"':'&quot;',"'":"&#39;",'*':'&#42;','%':'&#37;'}
    # #for key,value in specialCharDict.items():
        
    #     #text.replace(key,value)
    #     #strtoprint = self.specialCharDict["'"] if key == "'" else self.specialCharDict['"']
    #     #print(key, value)
    #     text = (text.replace('&','&#38;').replace('$','&#36;').replace('<','&lt;').replace('>','&gt;').
    #         replace('*','&#42;').replace('"','&quot;').replace("'","&#39;").replace('%','&#37;'))
    #     return text



# Start the main asyncio run
# try:
#     # logging.info("Running bot application...")
#     asyncio.run(run())
# except KeyboardInterrupt:
#     print("Ending bot application")# logging.info("Ending bot application")

print("JESUS IS LORD")

# if __name__ == "__main__":
#     um = UtilsMethods()
#     strtoparse = "FGX AU EQUITY Title : " \
#         "Future Generation $dollar &ampersand <br/>*star FY2023" \
#     "Results and Q&A Webinar Recording"
#     resultStr = um.text_parser(strtoparse)
#     print(resultStr)