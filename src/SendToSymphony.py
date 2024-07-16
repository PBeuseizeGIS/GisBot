import asyncio
import logging.config
from pathlib import Path

from symphony.bdk.core.config.loader import BdkConfigLoader
from symphony.bdk.core.symphony_bdk import SymphonyBdk

# Configure logging
current_dir = Path(__file__).parent.parent
logging_conf = Path.joinpath(current_dir, 'resources', 'logging.conf')
logging.config.fileConfig(logging_conf, disable_existing_loggers=False)

streamId = "wsXxwGntMFd87PnnKbcbu3___nCDx_PodA"
async def sendMessage():
  config = BdkConfigLoader.load_from_file(Path.joinpath(current_dir, 'resources', 'config.yaml'))
  async with SymphonyBdk(config) as bdk:
    name = "Patrick"
    response = f"<messageML>Hello {name}, hope you are doing well!</messageML>"
    await bdk.messages().send_message(streamId, response)
# try:
#   asyncio.run(sendMessage())
# except:
#  print("an error occured")
if __name__ == "__main__":
    try:
        sendMessage()
    except:
        print("ERROR OCCURRED")