# coding=utf-8

from fbchat import Client, ThreadType, Message #, log
import asyncio
import json

from var._collect import *
from var._urls import *
from functions.response import ResponseBy
from functions.response import Price
from functions.response_sku import TwinsShop, ChoiShop, FairyAngel


# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    async def on_message(self, author_id, message_object, thread_id, thread_type, **kwargs):
        # log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        # Ask for cod availability
        if message_object.text in askcod_list:
            
            await self.send(Message(text=ResponseBy.asking_cod_list()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="กรณีปฏิเสธการรับสินค้า มีความผิดนะจ้า"), thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls['imgs/cod.png'], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_cod'], thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="น้องขออนุญาติสรุปยอด\nพร้อมส่งเรทราคาสินค้าและค่าจัดส่งให้สักครู่นะจ้า"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)

        # Ask for more products
        if message_object.text in askmore_list:
            
            await self.send(Message(sticker=Sticker(ResponseBy.lovely_emoji())), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="มีจ้าคุณพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=tpl_urls['shop_page']), thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls['imgs/discount.jpg'], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_discount'], thread_id=thread_id, thread_type=thread_type)            
            await self.markAsUnread(thread_id)
        
        # Ask for price
        if message_object.text in askprice_list:

            await self.send(Message(text=ResponseBy.please_wait()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.asking_price_list()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(sticker=Sticker("2379835878707816")), thread_id=thread_id, thread_type=thread_type)
            #self.send(Message(text=ResponseBy.goto_lineadd()), thread_id=thread_id, thread_type=thread_type)
            await self.markAsUnread(thread_id)

        # Ask for size
        if message_object.text in asksize_list:
            
            await self.send(Message(text=ResponseBy.asking_size_list()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.please_wait()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(sticker=Sticker("2379835878707816")), thread_id=thread_id, thread_type=thread_type)
            #self.send(Message(text=ResponseBy.goto_lineadd()), thread_id=thread_id, thread_type=thread_type)
            await self.markAsUnread(thread_id)
        
        # Ask for Big Size
        if message_object.text in asksizebig_list:

            await self.send(Message(text=ResponseBy.asking_bigsize_list()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=tpl_urls['bigsize_page']), thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls[local_img_urls['imgs/discount.jpg']], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_discount'], thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(sticker=Sticker(ResponseBy.lovely_emoji())), thread_id=thread_id, thread_type=thread_type)            
            await self.markAsRead(thread_id)
        
        # Ask for COD method
        if message_object.text in cod_list:
            
            await self.send(Message(text="เงื่อนไขการสั่งซื้อสินค้าแบบเก็บเงินปลายทาง\n�1. การสั่งซื้อสินค้าแบบเก็บเงินปลายทางจะมีค่าบริการเพิ่ม\n�2. ห้ามปฏิเสธการรับของ เนื่องจากทางร้านจัดจำหน่าย และบริษัทขนส่งเกิดความเสียหาย ผู้สั่งสินค้ามีหน้าที่รับผิดชอบการสั่งซื้อสินค้า และชำระเงินตามยอดสั่งซื้อ\n\nอ่านก่อนติดสินใจสั่งซื้อ !! สั่งแล้วไม่รับ มีความผิด\n\n* หากไม่ชำระเงินหรือปฏิเสธการรับสินค้า จะมีความผิด ตามประมวลกฎหมายแพ่งและพาณิชย์ มาตรา 168 และ 458\n\nขอบพระคุณทุกท่านที่ไว้วางใจ และเลือกสินค้าของทางร้านเราค่ะ"), thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls['imgs/cod.png'], thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls['imgs/claim.png'], thread_id=thread_id, thread_type=thread_type)            
            await self.send_remote_files(remote_img_urls['img_cod'], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_claim'], thread_id=thread_id, thread_type=thread_type)            
            await self.send(Message(text="**หลังจากคอนเฟิร์มข้อมูลถูกต้องแล้ว ห้ามยกเลิกทุกกรณี**"), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="หากเข้าใจแล้วโปรดพิมพ์คำว่า \"ตกลง\""), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text in cod_confirm_list:
            
            await self.send(Message(text="น้องขอทราบ ชื่อ ที่อยู่ เบอร์โทรที่ติดต่อได้ ของคุณพี่ด้วยจ้า"), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="เพื่อป้องกันการตกหล่น น้องขอแบบพิมพ์นะจ้า"), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="หากให้ไว้แล้ว รอสักครู่นะจ้า"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)

        # Response for color
        if message_object.text in color_list or \
        message_object.text in color_not_list:
            
            await self.send(Message(text=ResponseBy.response_color()), thread_id=thread_id, thread_type=thread_type)            
            await self.send(Message(text=ResponseBy.please_wait()), thread_id=thread_id, thread_type=thread_type)            
            await self.send(Message(sticker=Sticker("2379835878707816")), thread_id=thread_id, thread_type=thread_type)
            #self.send(Message(text=ResponseBy.goto_lineadd()), thread_id=thread_id, thread_type=thread_type)
            await self.markAsUnread(thread_id)

        # First Message
        if message_object.text in init_list:

            await self.send(Message(text=ResponseBy.welcome_word_line_1()), thread_id=thread_id, thread_type=thread_type)            
            await self.send(Message(text=ResponseBy.welcome_word_line_2()), thread_id=thread_id, thread_type=thread_type)            
            await self.send(Message(text=ResponseBy.welcome_word_line_3()), thread_id=thread_id, thread_type=thread_type)
            
            # Use when long AFK
            await self.send(Message(text=ResponseBy.goto_lineadd()), thread_id=thread_id, thread_type=thread_type)
            #self.send(Message(text="หรือคุณพี่สามารถสั่งซื้อสินค้าด้วยตัวเองได้ที่นี่เลยนะจ้า\n\nhttps://www.theperfectladies.com/"), thread_id=thread_id, thread_type=thread_type)
            #self.send_remote_files(remote_img_urls['img_discount'], thread_id=thread_id, thread_type=thread_type)
            ##self.sendLocalImage(local_img_urls['imgs/discount.jpg'], thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
            
        # Found negative for bigsize
        if message_object.text in negative_bigsize_list:

            await self.send(Message(sticker=Sticker(ResponseBy.bad_emoji())), thread_id=thread_id, thread_type=thread_type)            
            await self.send(Message(text=ResponseBy.negative_bigsize_list()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=tpl_urls['bigsize_page']), thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls['imgs/discount.jpg'], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_discount'], thread_id=thread_id, thread_type=thread_type)            
            await self.markAsRead(thread_id)
        
        # Found aggressive messages
        if message_object.text in negative_list:

            await self.send(Message(sticker=Sticker(ResponseBy.bad_emoji())), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.negative_list()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=tpl_urls['shop_page']), thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls['imgs/discount.jpg'], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_discount'], thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        # Self Response
        if message_object.text in price_list:

            await self.send(Message(text="ส่งฟรี ลงทะเบียน จ้า"), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="สนใจรับสักชุดไหมจ้าคุณพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)

        # Found thankful messages
        if message_object.text in thankful_list:
            
            await self.send(Message(sticker=Sticker(ResponseBy.lovely_emoji())), thread_id=thread_id, thread_type=thread_type)            
            await self.send(Message(text=ResponseBy.thankful_word()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=tpl_urls['home_page']), thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls['imgs/discount.jpg'], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_discount'], thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
   
        # Ask for how to transfer
        if message_object.text in transfer_list:
            
            #self.sendLocalImage(local_img_urls['imgs/transfer.png'], thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls['imgs/claim.png'], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_transfer'], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_claim'], thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="โอนแล้วรบกวนแจ้งสลิป พร้อม ชื่อ ที่อยู่และเบอร์ติดต่อผู้รับ เพื่อจัดส่งชุดสวยๆให้ถึงมือคุณพี่ได้เลยจ้า😍"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)

        # Ask for shipping method
        if message_object.text == 'มีบริการส่งไหมคะ':

            await self.send(Message(text="มีบริการจัดส่งให้ฟรี ลทบ จ้า EMS เพิ่มอีกแค่ 30 บาท เท่านั้นจ้า"), thread_id=thread_id, thread_type=thread_type)            
            await self.markAsRead(thread_id)

        # Price Summary List
        if message_object.text == 'รวม390#1':
            
            await self.send(Message(text=Price.price_390_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม390#2':
            
            await self.send(Message(text=Price.price_390_2()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม780#1':
            
            await self.send(Message(text=Price.price_390x2()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม450#1':
            
            await self.send(Message(text=Price.price_450_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม490#1':
            
            await self.send(Message(text=Price.price_490_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม550#1':
            
            await self.send(Message(text=Price.price_550_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม590#1':
            
            await self.send(Message(text=Price.price_590_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม650#1':
            
            await self.send(Message(text=Price.price_650_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม690#1':
            
            await self.send(Message(text=Price.price_690_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)

        # Second Round
        if message_object.text == 'รวม370#1':
            
            await self.send(Message(text=Price.price_370_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม370#2':
            
            await self.send(Message(text=Price.price_370_2()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม740#1':
            
            await self.send(Message(text=Price.price_370x2()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม420#1':
            
            await self.send(Message(text=Price.price_420_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม470#1':
            
            await self.send(Message(text=Price.price_470_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม520#1':
            
            await self.send(Message(text=Price.price_520_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม570#1':
            
            await self.send(Message(text=Price.price_570_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม620#1':
            
            await self.send(Message(text=Price.price_620_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)
        elif message_object.text == 'รวม670#1':
            
            await self.send(Message(text=Price.price_670_1()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)


        # When finish everything
        if message_object.text == 'tq':
            
            await self.send(Message(text="หลังส่งของเสร็จ น้องขออนุญาตมาแจ้งเลขพัสดุ ไม่เกินวันพรุ่งนี้ ช่วงเวลา 22.00 น. ให้คุณพี่ทราบนะจ้า\n\nขอบพระคุณคุณพี่มากๆจ้า\n🙏"), thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage(local_img_urls['imgs/thxq.png'], thread_id=thread_id, thread_type=thread_type)
            await self.send_remote_files(remote_img_urls['img_thxq'], thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="📣 ช่วงนี้ เฟสบุ๊คทำการบล๊อคบัญชีบ่อย น้องขอความร่วมมือคุณพี่ แอดไลน์ 👉🏻📱 Line Official @theperfectladies\n\nหรือ กดลิ้งค์ด้านล่างนี้จ้า\n⬇⬇⬇\n\nhttp://nav.cx/8rtmakW\n\nได้ไหมจ้า ? เพื่อป้องกันไม่ให้พลาดการติดต่อจ้า 🙏🏻"), thread_id=thread_id, thread_type=thread_type)
            await self.markAsRead(thread_id)

        # Say sorry for late response
        if message_object.text == 'ขอประทานโทษที่ตอบช้านะจ้า':
            await self.send(Message(sticker=Sticker(ResponseBy.bad_emoji())), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.welcome_word_line_2()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=ResponseBy.do_you_still_want_this()), thread_id=thread_id, thread_type=thread_type)
            await self.markAsUnread(thread_id)

        if message_object.text in sku_twinsshop:
            tw = TwinsShop(message_object.text, message_object.text)
            await self.send_remote_files(tw.response_image(), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=tw.response_sku()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="ขนาดชุดตามนี้นะจ้า คุณพี่พอจะใส่ได้ไหมจ้า"), thread_id=thread_id, thread_type=thread_type)
        elif message_object.text in sku_choishop:
            cl = ChoiShop(message_object.text, message_object.text)
            await self.send_remote_files(cl.response_image(), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=cl.response_sku()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="ขนาดชุดตามนี้นะจ้า คุณพี่พอจะใส่ได้ไหมจ้า"), thread_id=thread_id, thread_type=thread_type)
        elif message_object.text in sku_fairyangel:
            fa = FairyAngel(message_object.text, message_object.text)
            await self.send_remote_files(fa.response_image(), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text=fa.response_sku()), thread_id=thread_id, thread_type=thread_type)
            await self.send(Message(text="ขนาดชุดตามนี้นะจ้า คุณพี่พอจะใส่ได้ไหมจ้า"), thread_id=thread_id, thread_type=thread_type)
