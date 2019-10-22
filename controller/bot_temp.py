# coding=utf-8

from fbchat import log, Client
from fbchat.models import *
from fbchat.models import Message

from var._collect import *
from functions.response import ResponseBy
from functions.response import Price


# Subclass fbchat.Client and override required methods
class EchoBotTemp(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        # Ask for cod availability
        if message_object.text in askcod_list:
            
            self.send(Message(text=ResponseBy.asking_cod_list()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="กรณีปฏิเสธการรับสินค้า มีความผิดนะจ้า"), thread_id=thread_id, thread_type=thread_type)
            self.sendLocalImage('imgs/cod.png', thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)

        # Ask for more products
        if message_object.text in askmore_list:

            self.send(Message(sticker=Sticker(ResponseBy.lovely_emoji())), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="มีจ้าคุณพี่"), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="https://www.theperfectladies.com/products/"), thread_id=thread_id, thread_type=thread_type)
            self.sendLocalImage('imgs/discount.png', thread_id=thread_id, thread_type=thread_type)
            self.markAsUnread(thread_id)

		# Ask for price
        if message_object.text in askprice_list:

            self.send(Message(text=ResponseBy.please_wait()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.asking_price_list()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.goto_lineadd()), thread_id=thread_id, thread_type=thread_type)
            self.markAsUnread(thread_id)

        # Ask for size
        if message_object.text in asksize_list:

            self.send(Message(text=ResponseBy.asking_size_list()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.please_wait()), thread_id=thread_id, thread_type=thread_type)
            self.markAsUnread(thread_id)
        
        # Ask for Big Size
        if message_object.text in asksizebig_list:

            self.send(Message(text=ResponseBy.asking_bigsize_list()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="https://www.theperfectladies.com/product-category/big-size/"), thread_id=thread_id, thread_type=thread_type)
            self.sendLocalImage('imgs/discount.png', thread_id=thread_id, thread_type=thread_type)
            self.send(Message(sticker=Sticker(ResponseBy.lovely_emoji())), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        
        # Ask for COD method
        if message_object.text in cod_list:
            
            self.send(Message(text="เงื่อนไขการสั่งซื้อสินค้าแบบเก็บเงินปลายทาง\n�1. การสั่งซื้อสินค้าแบบเก็บเงินปลายทางจะมีค่าบริการเพิ่ม\n�2. ห้ามปฏิเสธการรับของ เนื่องจากทางร้านจัดจำหน่าย และบริษัทขนส่งเกิดความเสียหาย ผู้สั่งสินค้ามีหน้าที่รับผิดชอบการสั่งซื้อสินค้า และชำระเงินตามยอดสั่งซื้อ\n\nอ่านก่อนติดสินใจสั่งซื้อ !! สั่งแล้วไม่รับ มีความผิด\n\n* หากไม่ชำระเงินหรือปฏิเสธการรับสินค้า จะมีความผิด ตามประมวลกฎหมายแพ่งและพาณิชย์ มาตรา 168 และ 458\n\nขอบพระคุณทุกท่านที่ไว้วางใจ และเลือกสินค้าของทางร้านเราค่ะ"), thread_id=thread_id, thread_type=thread_type)
            self.sendLocalImage('imgs/cod.png', thread_id=thread_id, thread_type=thread_type)
            self.sendLocalImage('imgs/claim.png', thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="**หลังจากคอนเฟิร์มข้อมูลถูกต้องแล้ว ห้ามยกเลิกทุกกรณี**"), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="หากเข้าใจแล้วโปรดพิมพ์คำว่า \"ตกลง\""), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text in cod_confirm_list:

            self.send(Message(text="น้องขอทราบ ชื่อ ที่อยู่ เบอร์โทรที่ติดต่อได้ ของคุณพี่ด้วยจ้า"), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="เพื่อป้องกันการตกหล่น น้องขอแบบพิมพ์นะจ้า"), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="หากให้ไว้แล้ว รอสักครู่นะจ้า"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)

        # Response for color
        if message_object.text in color_list or \
        message_object.text in color_not_list:

            self.send(Message(text=ResponseBy.response_color()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.please_wait()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.goto_lineadd()), thread_id=thread_id, thread_type=thread_type)
            self.markAsUnread(thread_id)

        # First Message
        if message_object.text in init_list:

            self.send(Message(text=ResponseBy.welcome_word_line_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.welcome_word_line_2()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.welcome_word_line_3()), thread_id=thread_id, thread_type=thread_type)
            self.addUsersToGroup([100012528676832, ], thread_id=thread_id)
            self.removeUserFromGroup(100006035379384, thread_id=thread_id)
            # Use when long AFK
            #self.send(Message(text=ResponseBy.goto_lineadd()), thread_id=thread_id, thread_type=thread_type)
            #self.send(Message(text="หรือคุณพี่สามารถสั่งซื้อสินค้าด้วยตัวเองได้ที่นี่เลยนะจ้า\n\nhttps://www.theperfectladies.com/"), thread_id=thread_id, thread_type=thread_type)
            #self.sendLocalImage('imgs/discount.png', thread_id=thread_id, thread_type=thread_type)
            #self.markAsRead(thread_id)
            
        # Found negative for bigsize
        if message_object.text in negative_bigsize_list:

            self.send(Message(sticker=Sticker(ResponseBy.bad_emoji())), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.negative_bigsize_list()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="https://www.theperfectladies.com/product-category/big-size/"), thread_id=thread_id, thread_type=thread_type)
            self.sendLocalImage('imgs/discount.png', thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        
        # Found aggressive messages
        if message_object.text in negative_list:

            self.send(Message(sticker=Sticker(ResponseBy.bad_emoji())), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.negative_list()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="https://www.theperfectladies.com/products/"), thread_id=thread_id, thread_type=thread_type)
            self.sendLocalImage('imgs/discount.png', thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        
        # Self Response
        if message_object.text in price_list:
            
            self.send(Message(text="ส่งฟรี ลงทะเบียน จ้า"), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="สนใจรับสักชุดไหมจ้าคุณพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)

        # Found thankful messages
        if message_object.text in thankful_list:

            self.send(Message(sticker=Sticker(ResponseBy.lovely_emoji())), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.thankful_word()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.goto_website()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="https://www.theperfectladies.com/"), thread_id=thread_id, thread_type=thread_type)
            self.sendLocalImage('imgs/discount.png', thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
   
        # Ask for how to transfer
        if message_object.text in transfer_list:

            self.sendLocalImage('imgs/transfer.png', thread_id=thread_id, thread_type=thread_type)
            self.sendLocalImage('imgs/claim.png', thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="โอนแล้วรบกวนแจ้งสลิป พร้อม ชื่อ ที่อยู่และเบอร์ติดต่อผู้รับ เพื่อจัดส่งชุดสวยๆให้ถึงมือคุณพี่ได้เลยจ้า😍"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)

        # Ask for shipping method
        if message_object.text == 'มีบริการส่งไหมคะ':

            self.send(Message(text="มีบริการจัดส่งให้ฟรี ลทบ จ้า EMS เพิ่มอีกแค่ 30 บาท เท่านั้นจ้า"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)

        
        # Price Summary List
        if message_object.text == 'รวม390#1':
            
            self.send(Message(text=Price.price_390_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม390#2':
            
            self.send(Message(text=Price.price_390_2()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม780#1':
            
            self.send(Message(text=Price.price_390x2()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม450#1':
            
            self.send(Message(text=Price.price_450_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม490#1':
            
            self.send(Message(text=Price.price_490_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม550#1':
            
            self.send(Message(text=Price.price_550_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม590#1':
            
            self.send(Message(text=Price.price_590_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม650#1':
            
            self.send(Message(text=Price.price_650_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม690#1':
            
            self.send(Message(text=Price.price_690_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
            

        # Second Round
        if message_object.text == 'รวม370#1':
            
            self.send(Message(text=Price.price_370_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม370#2':
            
            self.send(Message(text=Price.price_370_2()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม740#1':
            
            self.send(Message(text=Price.price_370x2()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม420#1':
            
            self.send(Message(text=Price.price_420_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม470#1':
            
            self.send(Message(text=Price.price_470_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม520#1':
            
            self.send(Message(text=Price.price_520_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม570#1':
            
            self.send(Message(text=Price.price_570_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม620#1':
            
            self.send(Message(text=Price.price_620_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
        elif message_object.text == 'รวม670#1':
            
            self.send(Message(text=Price.price_670_1()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text="คุณพี่สะดวกเลือกการจัดส่งแบบไหนดีจ้า\n\nสะดวก \"โอน\" หรือ \"ปลายทาง\" จ้าพี่"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)

        # When finish everything
        if message_object.text == 'tq':
            self.send(Message(text="หลังส่งของเสร็จ น้องขออนุญาตมาแจ้งเลขพัสดุ ไม่เกินวันพรุ่งนี้ ช่วงเวลา 22.00 น. ให้คุณพี่ทราบนะจ้า\n\nขอบพระคุณคุณพี่มากๆจ้า\n🙏"), thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)
            self.sendLocalImage('imgs/thxq.png', thread_id=thread_id, thread_type=thread_type)
            self.markAsRead(thread_id)

        # Say sorry for late response
        if message_object.text == 'ขอประทานโทษที่ตอบช้านะจ้า':
            self.send(Message(sticker=Sticker(ResponseBy.bad_emoji())), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.welcome_word_line_2()), thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.do_you_still_want_this()), thread_id=thread_id, thread_type=thread_type)
            self.markAsUnread(thread_id)